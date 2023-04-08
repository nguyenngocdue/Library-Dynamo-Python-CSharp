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


class Person:
    def __init__(self, name, age, mail):
        self.Name = name
        self.Age = age
        self.Mail = mail

class ViewModel:
    def __init__(self, peo):
        self.Name = peo.Name
        self.Age = peo.Age
        self.Mail = peo.Mail


class MyWindow(Window):
    def __init__(self, viewModel):
        self.ui = wpf.LoadComponent(self,  "A:\Library-Dynamo-Python-CSharp\Controls XAML\myform.xaml")
        self.lvUsers.ItemsSource = [ViewModel(peo) for peo in people]
        
    def fnBtnOk(self, sender, e):
        self.Close()
        
    def fnBtnCancel(self, sender, e):
       self.Close()

    def onSelectionChanged(self, sender, e):
        selected_item = self.lvUsers.SelectedItem
        if selected_item is not None:
            print("Selected item:", selected_item.Name, selected_item.Age, selected_item.Mail)

people = [Person("Alice", 25, "alice@example.com"),
       Person("Bob", 30, "bob@example.com")]
# print(people)
window = MyWindow(people)
showDialog = window.ShowDialog()