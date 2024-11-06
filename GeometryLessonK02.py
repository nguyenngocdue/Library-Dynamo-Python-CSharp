import clr
import System
import math 
from System.Collections.Generic import *

clr.AddReference('ProtoGeometry')
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
#############################################################################
def getList(inputValue):
    if isinstance(inputValue, list):
        return UnwrapElement(inputValue)
    else:
        return [UnwrapElement(inputValue)]
#############################################################################



def offsetPoints(line, dis):
    unit = 304.84
    startPoint = line.StartPoint #line.GetEndPoint(0)
    endPoint = line.EndPoint #line.GetEndPoint(1)
    x1, y1, z1 = startPoint.X + dis, startPoint.Y,  startPoint.Z
    x2, y2, z2 = endPoint.X + dis, endPoint.Y,  endPoint.Z

    return XYZ( x2-x1, y2-y1, z2-z1)

#############################################################################

objects = getList(IN[1])
result = [offsetPoints(obj, 1000) for obj in objects]

OUT = result
