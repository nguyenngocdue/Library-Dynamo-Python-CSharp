import clr
import System
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

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

x = IN[1]
y = IN[2]
z = IN[3]

TransactionManager.Instance.EnsureInTransaction(doc)

# Create Point XYZ
pts = []
for i1,i2,i3 in zip(x,y,z):
    pts.append(Point.ByCoordinates(i1,i2,i3))
#Get XYZ    
getXYZ = [i.ToXyz() for i in pts]

# Translate Point to ReferencePoint
refPoint = []
for i in getXYZ:
    var = doc.FamilyCreate.NewReferencePoint(i)
    refPoint.append(var)

TransactionManager.Instance.TransactionTaskDone()

OUT = refPoint