import os
import clr
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
# sys.path.append(r"C:\Users\NGUYEN NGOC DUE\AppData\Roaming\pyRevit\Extensions\BIM3DM.extension\lib\Bim3DM")
# import pyBIM3DMLab
#-------------------------------------------------------------------

def get_path_file():
    save_directory = os.path.expanduser("~/Documents") 
    file_name = "export_data.csv"
    file_path = os.path.join(save_directory, file_name)
    return file_path

class AllSheetsList():
    def get_sheets(self, doc):
        return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).ToElements()

class AllValuesSheets():
    def __init__(self, sheet):
        self.sheet = sheet
    
    @property
    def get_sheet_number(self):
        return self.sheet.get_Parameter(BuiltInParameter.SHEET_NUMBER).AsString()
    @property
    def get_sheet_name(self):
        return self.sheet.get_Parameter(BuiltInParameter.SHEET_NAME).AsString()
    @property
    def get_viewPorts(self):
        doc = __revit__.ActiveUIDocument.Document
        return FilteredElementCollector(doc, self.sheet.Id).OfCategory(BuiltInCategory.OST_Viewports).ToElements()
    @property
    def get_sheet_designer(self):
        return self.sheet.get_Parameter(BuiltInParameter.SHEET_DESIGNED_BY).AsString()
    @property
    def get_sheet_checked(self):
        return self.sheet.get_Parameter(BuiltInParameter.SHEET_CHECKED_BY).AsString()
    @property
    def get_sheet_draw(self):
        return self.sheet.get_Parameter(BuiltInParameter.SHEET_DRAWN_BY).AsString()
    @property
    def get_sheet_date(self):
        return self.sheet.get_Parameter(BuiltInParameter.SHEET_ISSUE_DATE).AsString()
    @property
    def count_views(self):
        num_views = len(set(vp.ViewId for vp in self.get_viewPorts))
        return num_views
    

# get all viewports in the sheet
#-------------------------------------------------------------------
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument 
app = __revit__.Application 

allSheets = AllSheetsList().get_sheets(doc)

dictSheets = [{        "count" : n,
                        "sheet_number" :AllValuesSheets(s).get_sheet_number,
                        "sheet_name" : AllValuesSheets(s).get_sheet_name,
                        "amount_view" :AllValuesSheets(s).count_views,
                        "designer" :AllValuesSheets(s).get_sheet_designer,
                        "drawnBy" :AllValuesSheets(s).get_sheet_draw,
                        "checked" :AllValuesSheets(s).get_sheet_checked,
                        "date" :AllValuesSheets(s).get_sheet_date
                        } for s, n in zip(allSheets, range(len(allSheets)))]
# print(dictSheets)

class Sheet:
    def __init__(self,sheet):
        self.count = sheet["count"]
        self.sheet_number = sheet["sheet_number"]
        self.sheet_name = sheet["sheet_name"]
        self.amount_view = sheet["amount_view"]
        self.designer = sheet["designer"]
        self.drawnBy = sheet["drawnBy"]
        self.checked = sheet["checked"]
        self.date = sheet["date"]

class ViewModel:
    def __init__(self, sheets):
        self.sheets = sheets
        self.gvcCount = sheets.count
        self.gvcSheetNumber = sheets.sheet_number
        self.gvcSheetName = sheets.sheet_name
        self.gvcAmountView = sheets.amount_view
        self.gvcDesigner = sheets.designer
        self.gvcDrawnBy = sheets.drawnBy
        self.gvcChecked = sheets.checked
        self.gvcDate = sheets.date

class MyWindow(Window):
    def __init__(self, viewModel):
        self.ui = wpf.LoadComponent(self, r"C:\Users\NGUYEN NGOC DUE\AppData\Roaming\pyRevit\Extensions\pyBIM3DM.extension\pyBIM3DM.tab\List View.panel\Export Data.pushbutton\form.xaml")
        self.lvUsers.ItemsSource = [ViewModel(s) for s in sheets]

    def btnExport(self, sender, event):
        with forms.WarningBar(title='Export Data To Excel:'):
            path = get_path_file()
            with open(path, "w") as file:
                writer = csv.writer(file)
                columnName = dictSheets[0].keys()
                writer.writerow([col.encode("utf-8") for col in columnName])  
                max_value = len(sheets)
                with ProgressBar(title='My Process... ({value} of {max_value})') as pb:
                    for counter in range(0, max_value):
                        pb.update_progress(counter, max_value)
                        item = sheets[counter]
                        writer.writerow([
                            item.count,
                            item.sheet_number.encode("utf-8"),
                            item.sheet_name.encode("utf-8"),
                            item.amount_view,
                            item.designer.encode("utf-8"),
                            item.drawnBy.encode("utf-8"),
                            item.checked.encode("utf-8"),
                            item.date.encode("utf-8"),
                        ])
            os.startfile(path)
        self.Close()
    def btnCancel(self, sender, event):
        self.Close()


sheets = [Sheet(s) for s in dictSheets]

MyWindow(sheets).ShowDialog()