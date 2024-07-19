import clr
clr.AddReference("System")   
import System
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import*
from Autodesk.Revit.DB import Transaction, FilteredElementCollector
from System.Collections.Generic import List

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#########################################################################

import wpf
from System.Windows import Application, Window
from System.Windows.Data import Binding
#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#########################################################################

class ViewModel:
    def __init__(self):
        pass
class MyWindow(Window):
    def __init__(self, viewModel):
        self.ui = wpf.LoadComponent(self, r"U:\17_TraningAdvanceDynamo\2_WORKING\Tool\Design\ConfigSelections\config_view.xaml")

viewModel = ViewModel()
window = MyWindow(viewModel)
showDialog = window.ShowDialog()