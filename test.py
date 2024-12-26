"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
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
#Build a new empty Category List...
cate_List = List[BuiltInCategory]()
#Only Add some Element Types to cate_List...
cate_List.Add(BuiltInCategory.OST_StructuralFraming)
cate_List.Add(BuiltInCategory.OST_StructuralColumns)
cate_List.Add(BuiltInCategory.OST_StructuralFoundation)
cate_List.Add(BuiltInCategory.OST_Floors)
cate_List.Add(BuiltInCategory.OST_Walls)
cate_List.Add(BuiltInCategory.OST_Windows)
cate_List.Add(BuiltInCategory.OST_Doors)

result = []
for b in cate_List:
    ele = FilteredElementCollector(doc).OfCategory(b).WhereElementIsNotElementType().ToElements()
    result.append(ele)
OUT = cate_List


