"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
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

from Autodesk.DesignScript.Geometry import Line, Point
def lstFlattenL2(list):
    result = []
    for i in list:
        for j in i:
            result.append(j)
    return result


ele1 =  lstFlattenL2(UnwrapElement(IN[0]))
eles =  lstFlattenL2(UnwrapElement(IN[1]))
intersect = [ele1[0].DoesIntersect(i) for i in eles]

inter_lines = []
not_inter_lines = []
for line, inters  in zip(eles, intersect):
	if (inters):
		inter_lines.append(line)
	else: not_inter_lines.append(line)



OUT =  inter_lines, not_inter_lines
