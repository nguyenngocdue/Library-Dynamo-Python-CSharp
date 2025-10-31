"""Reusable WPF forms for pyRevit.

Example:
    >>> from pyrevit.forms import WPFWindow
"""

import sys
import os
import os.path as op
import string
from collections import OrderedDict, namedtuple
import threading
from functools import wraps
import datetime
import webbrowser


from pyrevit import coreutils
from pyrevit import framework
from pyrevit.framework import System
from pyrevit.framework import Threading
from pyrevit.framework import Interop
from pyrevit.framework import Input
from pyrevit.framework import wpf, Forms, Controls, Media
from pyrevit.framework import CPDialogs
from pyrevit.framework import ComponentModel
from pyrevit.framework import ObservableCollection
from pyrevit.api import AdWindows
from pyrevit import revit, UI, DB
from pyrevit.forms import utils
from pyrevit.forms import toaster
from pyrevit import versionmgr
from rpw.ui.forms import select_file
from pyrevit import HOST_APP, EXEC_PARAMS, DOCS, BIN_DIR
from pyrevit import PyRevitCPythonNotSupported, PyRevitException, PyRevitCPythonNotSupported

DEFAULT_INPUTWINDOW_WIDTH = 500
DEFAULT_INPUTWINDOW_HEIGHT = 600
DEFAULT_CMDSWITCHWND_WIDTH = 600
DEFAULT_SEARCHWND_WIDTH = 600
DEFAULT_SEARCHWND_HEIGHT = 100
DEFAULT_INPUTWINDOW_HEIGHT = 600
DEFAULT_RECOGNIZE_ACCESS_KEY = False

XAML_FILES_DIR = op.dirname(__file__)

class WPFWindow(framework.Windows.Window):
    r"""WPF Window base class for all pyRevit forms.

    Args:
        xaml_source (str): xaml source filepath or xaml content
        literal_string (bool): xaml_source contains xaml content, not filepath
        handle_esc (bool): handle Escape button and close the window
        set_owner (bool): set the owner of window to host app window

    Example:
        >>> from pyrevit import forms
        >>> layout = '<Window ' \
        >>>          'xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" ' \
        >>>          'xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" ' \
        >>>          'ShowInTaskbar="False" ResizeMode="NoResize" ' \
        >>>          'WindowStartupLocation="CenterScreen" ' \
        >>>          'HorizontalContentAlignment="Center">' \
        >>>          '</Window>'
        >>> w = forms.WPFWindow(layout, literal_string=True)
        >>> w.show()
    """

    def __init__(self, xaml_source, literal_string=False, handle_esc=True, set_owner=True):
        """Initialize WPF window and resources."""
        # load xaml
        self.load_xaml(
            xaml_source,
            literal_string=literal_string,
            handle_esc=handle_esc,
            set_owner=set_owner
            )

    def load_xaml(self, xaml_source, literal_string=False, handle_esc=True, set_owner=True):
        # create new id for this window
        self.window_id = coreutils.new_uuid()

        if not literal_string:
            if not op.exists(xaml_source):
                wpf.LoadComponent(self,
                                  os.path.join(EXEC_PARAMS.command_path,
                                               xaml_source))
            else:
                wpf.LoadComponent(self, xaml_source)
        else:
            wpf.LoadComponent(self, framework.StringReader(xaml_source))

        # set properties
        self.thread_id = framework.get_current_thread_id()
        if set_owner:
            self.setup_owner()
        self.setup_icon()
        WPFWindow.setup_resources(self)
        if handle_esc:
            self.setup_default_handlers()

    def setup_owner(self):
        wih = Interop.WindowInteropHelper(self)
        wih.Owner = AdWindows.ComponentManager.ApplicationWindow

    @staticmethod
    def setup_resources(wpf_ctrl):
        #2c3e50
        wpf_ctrl.Resources['pyRevitDarkColor'] = \
            Media.Color.FromArgb(0xFF, 0x2c, 0x3e, 0x50)

        #23303d
        wpf_ctrl.Resources['pyRevitDarkerDarkColor'] = \
            Media.Color.FromArgb(0xFF, 0x23, 0x30, 0x3d)

        #ffffff
        wpf_ctrl.Resources['pyRevitButtonColor'] = \
            Media.Color.FromArgb(0xFF, 0xff, 0xff, 0xff)

        #f39c12
        wpf_ctrl.Resources['pyRevitAccentColor'] = \
            Media.Color.FromArgb(0xFF, 0xf3, 0x9c, 0x12)

        wpf_ctrl.Resources['pyRevitDarkBrush'] = \
            Media.SolidColorBrush(wpf_ctrl.Resources['pyRevitDarkColor'])
        wpf_ctrl.Resources['pyRevitAccentBrush'] = \
            Media.SolidColorBrush(wpf_ctrl.Resources['pyRevitAccentColor'])

        wpf_ctrl.Resources['pyRevitDarkerDarkBrush'] = \
            Media.SolidColorBrush(wpf_ctrl.Resources['pyRevitDarkerDarkColor'])

        wpf_ctrl.Resources['pyRevitButtonForgroundBrush'] = \
            Media.SolidColorBrush(wpf_ctrl.Resources['pyRevitButtonColor'])

        wpf_ctrl.Resources['pyRevitRecognizesAccessKey'] = \
            DEFAULT_RECOGNIZE_ACCESS_KEY

    def setup_default_handlers(self):
        self.PreviewKeyDown += self.handle_input_key    #pylint: disable=E1101

    def handle_input_key(self, sender, args):    #pylint: disable=W0613
        """Handle keyboard input and close the window on Escape."""
        if args.Key == Input.Key.Escape:
            self.Close()

    def set_icon(self, icon_path):
        """Set window icon to given icon path."""
        self.Icon = utils.bitmap_from_file(icon_path)

    def setup_icon(self):
        """Setup default window icon."""
        self.set_icon(op.join(BIN_DIR, 'pyrevit_settings.png'))

    def hide(self):
        self.Hide()

    def show(self, modal=False):
        """Show window."""
        if modal:
            return self.ShowDialog()
        # else open non-modal
        self.Show()

    def show_dialog(self):
        """Show modal window."""
        return self.ShowDialog()

    @staticmethod
    def set_image_source_file(wpf_element, image_file):
        """Set source file for image element.

        Args:
            element_name (System.Windows.Controls.Image): xaml image element
            image_file (str): image file path
        """
        if not op.exists(image_file):
            wpf_element.Source = \
                utils.bitmap_from_file(
                    os.path.join(EXEC_PARAMS.command_path,
                                 image_file)
                    )
        else:
            wpf_element.Source = utils.bitmap_from_file(image_file)

    def set_image_source(self, wpf_element, image_file):
        """Set source file for image element.

        Args:
            element_name (System.Windows.Controls.Image): xaml image element
            image_file (str): image file path
        """
        WPFWindow.set_image_source_file(wpf_element, image_file)

    def dispatch(self, func, *args, **kwargs):
        if framework.get_current_thread_id() == self.thread_id:
            t = threading.Thread(
                target=func,
                args=args,
                kwargs=kwargs
                )
            t.start()
        else:
            # ask ui thread to call the func with args and kwargs
            self.Dispatcher.Invoke(
                System.Action(
                    lambda: func(*args, **kwargs)
                    ),
                Threading.DispatcherPriority.Background
                )

    def conceal(self):
        return WindowToggler(self)

    @property
    def pyrevit_version(self):
        """Active pyRevit formatted version e.g. '4.9-beta'"""
        return 'pyRevit {}'.format(
            versionmgr.get_pyrevit_version().get_formatted()
            )

    @staticmethod
    def hide_element(*wpf_elements):
        """Collapse elements.

        Args:
            *wpf_elements: WPF framework elements to be collaped
        """
        for wpfel in wpf_elements:
            wpfel.Visibility = WPF_COLLAPSED

    @staticmethod
    def show_element(*wpf_elements):
        """Show collapsed elements.

        Args:
            *wpf_elements: WPF framework elements to be set to visible.
        """
        for wpfel in wpf_elements:
            wpfel.Visibility = WPF_VISIBLE

    @staticmethod
    def toggle_element(*wpf_elements):
        """Toggle visibility of elements.

        Args:
            *wpf_elements: WPF framework elements to be toggled.
        """
        for wpfel in wpf_elements:
            if wpfel.Visibility == WPF_VISIBLE:
                WPFWindow.hide_element(wpfel)
            elif wpfel.Visibility == WPF_COLLAPSED:
                WPFWindow.show_element(wpfel)

    @staticmethod
    def disable_element(*wpf_elements):
        """Enable elements.

        Args:
            *wpf_elements: WPF framework elements to be enabled
        """
        for wpfel in wpf_elements:
            wpfel.IsEnabled = False

    @staticmethod
    def enable_element(*wpf_elements):
        """Enable elements.

        Args:
            *wpf_elements: WPF framework elements to be enabled
        """
        for wpfel in wpf_elements:
            wpfel.IsEnabled = True

    def handle_url_click(self, sender, args): #pylint: disable=unused-argument
        """Callback for handling click on package website url"""
        return webbrowser.open_new_tab(sender.NavigateUri.AbsoluteUri)



class TemplateUserInputWindow(WPFWindow):
    """Base class for pyRevit user input standard forms.

    Args:
        context (any): window context element(s)
        title (str): window title
        width (int): window width
        height (int): window height
        **kwargs: other arguments to be passed to :func:`_setup`
    """

    xaml_source = 'BaseWindow.xaml'

    def __init__(self, context, title, width, height, **kwargs):
        """Initialize user input window."""
        WPFWindow.__init__(self,
                           op.join(XAML_FILES_DIR, self.xaml_source),
                           handle_esc=True)
        self.Title = title or 'pyRevit'
        self.Width = width
        self.Height = height

        self._context = context
        self.response = None

        # parent window?
        owner = kwargs.get('owner', None)
        if owner:
            # set wpf windows directly
            self.Owner = owner
            self.WindowStartupLocation = \
                framework.Windows.WindowStartupLocation.CenterOwner

        self._setup(**kwargs)

    def _setup(self, **kwargs):
        """Private method to be overriden by subclasses for window setup."""
        pass

    @classmethod
    def show(cls, context,  #pylint: disable=W0221
             title='User Input',
             width=DEFAULT_INPUTWINDOW_WIDTH,
             height=DEFAULT_INPUTWINDOW_HEIGHT, **kwargs):
        """Show user input window.

        Args:
            context (any): window context element(s)
            title (str): window title
            width (int): window width
            height (int): window height
            **kwargs (any): other arguments to be passed to window
        """
        dlg = cls(context, title, width, height, **kwargs)
        dlg.ShowDialog()
        return dlg.response

class AddScriptDynamo(TemplateUserInputWindow):
    xaml_source = 'AddScriptDynamo.xaml'
    def _setup(self, **kwargs):
        self.cbx_select_files.ItemsSource = ['.dyn', '.py']
        self.cbx_select_files.SelectionChanged += self.selectionChangedFiles

    def btnSelectIcon(self, sender, event):
        filePath = select_file('icon separated by semicolon (*.icon,*.jpg,*.jpeg,*.png)|*.icon;*.jpg;*.jpeg;*.png')
        self.txtb_icon_path.Text = filePath
    
    def selectionChangedFiles(self, sender, event):
        from System.Windows import Visibility
        selected_item = self.cbx_select_files.SelectedItem
        if selected_item in ['.dyn']:
            self.panel_file.Visibility = Visibility.Visible
            prompt = "{0} separated by semicolon (*{0})|*{0}".format(selected_item)
            filePath = select_file(prompt)
            self.txtb_dyn_path.Text = filePath

        else:
            self.panel_file.Visibility = Visibility.Collapsed
    def btnOK(self, sender, event):
        self.Close()
        self.response = {
                            "txtPanel_name" : self.txtPanel_name.Text,
                            "txtTool_name" : self.txtTool_name.Text,
                            "txtb_dyn_path" : self.txtb_dyn_path.Text,
                            "txtb_icon_path" : self.txtb_icon_path.Text
                        }
    def btnCancel(self, sender, event):
        self.Close()
        self.response = []




def ask_DynamoScript(items = [], default=None,prompt=None, title="Create a Custom Toolbar Button", **kwargs):
    return AddScriptDynamo.show(
        items,
        default=default,
        prompt=prompt,
        title=title,
        width = 610,
        **kwargs
        )

