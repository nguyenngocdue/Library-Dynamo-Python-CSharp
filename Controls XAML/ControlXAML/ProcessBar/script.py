import clr
clr.AddReference("System")   
import System
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import*
from Autodesk.Revit.DB import Transaction, FilteredElementCollector
from pyrevit import revit, forms
from System.Collections.Generic import List

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*


clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from pyrevit import DB

#----------------------------------------------------------------------
import time
import clr
clr.AddReference("PresentationFramework")
from System.Windows import *
from System.Windows.Controls import *

#----------------------------------------------------------------------
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument 
app = __revit__.Application 
__title__ = "PyBIM3DM" 

import wpf
from System.Windows import Application, Window
from System.Windows.Data import Binding


class ViewModel:
    def __init__(self):
        self._progressBarValue = 0

    @property
    def ProgressBarValue(self):
        return self._progressBarValue

    @ProgressBarValue.setter
    def ProgressBarValue(self, value):
        self._progressBarValue = value

    def run_process(self):
        for i in range(100):
            self.ProgressBarValue = i + 1
            print("{}test%".format(self.ProgressBarValue))
            time.sleep(0.1)


class MyWindow(Window):
    def __init__(self, viewModel):
        self.viewModel = viewModel  # set the view model to an instance variable
        self.ui = wpf.LoadComponent(self, "A:\Library-Dynamo-Python-CSharp\Controls XAML\myform.xaml")
        self.ui.DataContext = viewModel
        self.progressText.Text = "000%"

        # Bind the ProgressBarValue property to the ProgressBar control
        self.progressBar.SetBinding(ProgressBar.ValueProperty, Binding("ProgressBarValue"))

    def fnBtnOk(self, sender, e):
        self.ProgressBarValue = "100"
        for i in range(100):
            self.progressText.Text = str(i) + 'a'
            time.sleep(0.1)

    def fnBtnCancel(self, sender, e):
        self.Close()

viewModel = ViewModel()
window = MyWindow(viewModel)
window.ShowDialog()


