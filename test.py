"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
import System
sys.path.append(r'A:\Library-Dynamo-Python-CSharp')
import math 
from System.Collections.Generic import *

from DynamoVN import *


clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*
from  Autodesk.Revit.UI.Selection import ISelectionFilter

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#############################################################################
def getList(inputValue):
    if isinstance(inputValue, list):
        return UnwrapElement(inputValue)
    else:
        return [UnwrapElement(inputValue)]
#############################################################################

naCate = [i.Name for i in doc.Settings.Categories]
fil = "Schedules"
getIndex_Item = naCate.index(fil)
catebyName = UnwrapElement(Revit.Elements.Category.ByName(naCate[getIndex_Item]))

bic = System.Enum.ToObject(BuiltInCategory, catebyName.Id.IntegerValue)
scheName = FilteredElementCollector(doc).OfCategory(bic).ToElements()
OUT = scheName

path = r"U:\24_OneDrive\OneDrive\Desktop\Untitled Project"
result_list = []
for index, sched in enumerate(scheName):
    schedule = UnwrapElement(sched)
    fileName = schedule.Name + ".xls"
    try:
        export_options = ViewScheduleExportOptions()
        
        schedule.Export(path,fileName,export_options)

        result_list.append("Schedule Exported "+ fileName)
    except:
        result_list.append("Eport Failure" + fileName)