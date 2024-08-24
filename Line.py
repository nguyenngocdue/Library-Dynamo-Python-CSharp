import clr 
import System
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
from Autodesk.DesignScript.Geometry import PolyCurve, Line

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
from Autodesk.DesignScript.Geometry import Line
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#########################################################################
def getXyzItemsByOffsetPointsFromDbLines(lines, deltaX = 0, deltaY = 0, deltaZ =0):
    xyzItems = []
    for line in lines:
        startPoint = line.GetEndPoint(0)
        endPoint = line.GetEndPoint(1)
        newStartPoint = XYZ(startPoint.X - deltaX, startPoint.Y - deltaY,startPoint.Z - deltaZ )
        endStartPoint = XYZ(endPoint.X - deltaX, endPoint.Y - deltaY,endPoint.Z - deltaZ )
        xyzItems.append([newStartPoint, endStartPoint])
    return xyzItems

deltaX = IN[1]/304.8
deltaY = IN[2]/304.8
deltaZ = IN[3]/304.8
OUT = getXyzItemsByOffsetPointsFromDbLines(IN[0], deltaX, deltaY, deltaZ)

