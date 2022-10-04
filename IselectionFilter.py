
"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
__doc__ = '.........'
__author__ = 'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
__title__ = '.....'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
sys.path.append(r'C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\IronPython.StdLib.2.7.8')
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
###############################################################################
class SelectionFilter(ISelectionFilter):
    def __init__(self, ctgName1 , ctgName2):
        self.ctgName1 = ctgName1
        self.ctgName2 = ctgName2
    def AllowElement(self, element):
        if element.Category.Name == self.ctgName1 or element.Category.Name == self.ctgName2:
            return True
        else:
            return False
    def AllowReference(ref, xyZ):
        return False


ele = SelectionFilter("Structural Columns", "Structural Framing")
elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")

eleFraming = []
eleColumn = []
eleAll = []

for i in elSelectAll:
    try:
        if i.Category.Name == "Structural Framing":
            eleFraming.append(i)
        if i.Category.Name == "Structural Columns":
            eleColumn.append(i)
        if i.Category.Name == "Structural Columns" or i.Category.Name == "Structural Framing":
            eleAll.append(i)
    except:
        pass


OUT = eleFraming,eleColumn



re  = open(r"A:\TRAINING DYNAMO API\PART 7 SHARE\reView\SelectionFilter.py","r")
interpret = re.read()
OUT = interpret