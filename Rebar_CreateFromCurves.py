"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
import clr 
import System
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
from Autodesk.DesignScript.Geometry import Line, Point
from Autodesk.DesignScript.Geometry import GeometryExtension

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
from Autodesk.Revit.DB.Structure import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
import math

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
################################################################
def getDBLineFormEleLine(ElementLines): # Get Revit.DB.Line from Curve Elements
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    ln = []
    for i in ElementLines:
        ln.append(UnwrapElement(i).ToRevitType())
    return ln
def getVectorOfDBLine(lstDBline): # Get Vector from DBLine
    vec = []
    for i in lstDBline:
        pts1Line = i.GetEndPoint(0)
        pts2Line = i.GetEndPoint(1)
        vec.append(pts1Line - pts2Line)
    return vec



curves = UnwrapElement(IN[1])
element = UnwrapElement(IN[2])
rebarStyle = IN[3]
rebarType = UnwrapElement(IN[4])
hookTypeStart = UnwrapElement(IN[5])
hookTypeEnd = UnwrapElement(IN[6])
rebarHookOrientationStart = UnwrapElement(IN[7])
rebarHookOrientationEnd = UnwrapElement(IN[8])
normal = XYZ(1,0,0)

dbLines = getDBLineFormEleLine(curves)

vectorDBlines = getVectorOfDBLine(dbLines)


rebars = []
TransactionManager.Instance.EnsureInTransaction(doc)
for index, curve in enumerate(dbLines): 
    rebar = Rebar.CreateFromCurves(doc, 
                                    rebarStyle, 
                                    rebarType, 
                                    hookTypeStart, 
                                    hookTypeEnd, 
                                    element, 
                                    normal, 
                                    List[Curve]([curve]), 
                                    rebarHookOrientationStart, 
                                    rebarHookOrientationEnd, 
                                    True, 
                                    True)            
    rebars.append(rebar)
TransactionManager.Instance.TransactionTaskDone()
OUT = rebars
