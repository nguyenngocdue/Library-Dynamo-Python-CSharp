# WPF
try:
    clr.AddReference("IronPython.wpf")
    clr.AddReference('PresentationCore')
    clr.AddReference('PresentationFramework')
except IOError:
    raise
from System.IO import StringReader
from System.Windows.Markup import XamlReader, XamlWriter
from System.Windows import Window, Application, MessageBox, MessageBoxButton, MessageBoxResult
from System.Windows import RoutedEventHandler
from System.Runtime.InteropServices import Marshal
try:
    import wpf
except ImportError:
    raise

#----------------------------------------------------------------
