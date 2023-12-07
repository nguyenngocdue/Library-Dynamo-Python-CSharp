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
#########################################################################
def is_array(obj):
    return "List" in obj.__class__.__name__ or "list" in obj.__class__.__name__ 

def get_array_rank(array):
    if is_array(array):
        return 1 + max(get_array_rank(item) for item in array)
    else:
        return 0
def flatten_to_1d(arr):
    result = []
    def recursive_flatten(subarray):
        for item in subarray:
            if is_array(item):
                recursive_flatten(item)
            else:
                result.append(item)

    recursive_flatten(arr)
    return result
def returnOUT(fn, objects):
    rank = get_array_rank(objects)
    if rank == 0:  # a
        return fn(objects)
    elif rank == 1:  # [a]
        return [fn(*args) for args in objects]
    elif rank == 2:  # [[a]]
        return [fn(*i) for i in objects for i in j]
    else:
        elements = flatten_to_1d(objects)  # [a]
        return fn(elements)


#########################################################################
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
#########################################################################
curves = UnwrapElement(IN[1])
rank = get_array_rank(curves)
if rank == 0: curves = [curves]

element = UnwrapElement(IN[2])
rebarShape = UnwrapElement(IN[3])
rebarType = UnwrapElement(IN[4])
hookTypeStart = UnwrapElement(IN[5])
hookTypeEnd = UnwrapElement(IN[6])
rebarHookOrientationStart = UnwrapElement(IN[7])
rebarHookOrientationEnd = UnwrapElement(IN[8])
normal = IN[9]
rankNormal = get_array_rank(normal) 
normals = [normal] if rankNormal == 0 else normal

dbLines = getDBLineFormEleLine(curves)

vectorDBlines = getVectorOfDBLine(dbLines)


rebars = []
TransactionManager.Instance.EnsureInTransaction(doc)
for index, curve in enumerate(dbLines): 
    rebar = Rebar.CreateFromCurvesAndShape(doc,
                                    rebarShape,
                                    rebarType, 
                                    hookTypeStart, 
                                    hookTypeEnd, 
                                    element, 
                                    normals[index], 
                                    List[Curve]([curve]), 
                                    rebarHookOrientationStart, 
                                    rebarHookOrientationEnd, 
                                    )            
    rebars.append(rebar)
TransactionManager.Instance.TransactionTaskDone()
OUT = rebars
