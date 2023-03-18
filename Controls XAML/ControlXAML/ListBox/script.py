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
from pyrevit import forms
#----------------------------------------------------------------------
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument 
app = __revit__.Application 
__title__ = "PyBIM3DM" 

import wpf
from System.Windows import Application, Window
from System.Windows.Data import Binding




class ViewModel:
    def __init__(self, *args):
        self.data = data


class MyWindow(Window):
    def __init__(self, viewModel):
        self.ui = wpf.LoadComponent(self,  "A:\Library-Dynamo-Python-CSharp\Controls XAML\myform.xaml")
        self.ui.DataContext= viewModel
        

    def fnBtnOk(self, sender, e):
        selected_items = []
        for item in self.lstBoxName.SelectedItems:
            selected_items.append(item)
        print(selected_items)

        self.Close()
    def fnBtnCancel(self, sender, e):
       self.Close()
data = [1, 2, 3, 4, 5, 7, 8, 9, 10]
viewModel = ViewModel()
window = MyWindow(viewModel)
showDialog = window.ShowDialog()