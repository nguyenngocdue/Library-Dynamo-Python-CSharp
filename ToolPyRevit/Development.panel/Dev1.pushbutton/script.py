import os
import clr
import json
clr.AddReference("System")   
import System
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import*
from Autodesk.Revit.DB import Transaction, FilteredElementCollector
from pyrevit import revit, forms, DB, framework
from System.Collections.Generic import List

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*
from pyrevit.forms import ProgressBar


clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#-------------------------------------------------------------------
from System.Windows import Window
from System.Windows.Interop import WindowInteropHelper
import wpf
from System.Windows import Application, Window
from System.Windows.Data import Binding
import csv
#-------------------------------------------------------------------
import sys 
sys.path.append(r"C:\Users\NGUYEN NGOC DUE\AppData\Roaming\pyRevit\Extensions\BIM3DM.extension\lib\Bim3DM")

# get all viewports in the sheet
#-------------------------------------------------------------------
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument 
app = __revit__.Application 
#-------------------------------------------------------------------
buttonPath = r'C:\Users\NGUYEN NGOC DUE\AppData\Roaming\pyRevit\Extensions\pyOpenDyn.extension\pyOpenDyn.tab\Development.panel\Dev1.pushbutton'
formPath = os.path.join(buttonPath, "form.xaml")
userSetingPath = os.path.join(buttonPath, "user_setting.json")

class CategoryRevit():
    def getAllCategories(self, doc):
        categories = doc.Settings.Categories
        return [category for category in categories]
class QueeriedCategory():
    def __init__(self, category):
        self.category = category
    @property
    def getName(self):
        return self.category.Name
    
revitCats = CategoryRevit().getAllCategories(doc)
categoryNames = sorted([QueeriedCategory(cat).getName for cat in revitCats]) 
dictCats = [
                {
                    "count" : i + 1,
                    "category_name" : categoryNames[i],
                    "paramter_filter" : '{}',
                } for i in range(len(revitCats))
            ]
class CategoryDataSource:
    def __init__(self,category):
        self.count = category["count"]
        self.category_name = category["category_name"]
        self.gvcIsActive = category.get("is_active", False)
        self.paramter_filter = category["paramter_filter"]

#maping data to UI
class ViewModel:
    def __init__(self, category):
        self.category = category
        self.gvcCount = category.count
        self.gvcCategoryOst = category.category_name
        self.gvcParameterJson = category.paramter_filter
        self.gvcIsActive = category.gvcIsActive
class MyWindow(Window):
    def __init__(self, viewModel):
        self.ui = wpf.LoadComponent(self, formPath)
        self.lvUsers.ItemsSource = [ViewModel(cat) for cat in categories]
    def txtSearchTextChanged(self, sender, event):
        searchQuery = sender.Text.lower()
        self.filteredCategories = [
            ViewModel(cat) for cat in categories
            if searchQuery in cat.category_name.lower() or searchQuery in cat.paramter_filter.lower()
        ]
        self.lvUsers.ItemsSource = self.filteredCategories
    def btnApply(self, sender, event):
       # Collect all selected items from the ListView (rows with the checkbox checked)
        selectedItems = [ item for item in self.lvUsers.ItemsSource]
        # Create a JSON data structure from the selected items
        data = [
            {
                "count": item.gvcCount,
                "category_name": item.gvcCategoryOst,
                "parameter_filter": item.gvcParameterJson,
                "is_active": item.gvcIsActive
            }
            for item in selectedItems
        ]
        jsonData = json.dumps(data, indent=4)
        
        #Write the JSON data to the file
        with open(userSetingPath, "w") as json_file:
            json_file.write(jsonData)
    def btnCancel(self, sender, event):
        self.Close()

categories = [CategoryDataSource(s) for s in dictCats]
MyWindow(categories).ShowDialog()