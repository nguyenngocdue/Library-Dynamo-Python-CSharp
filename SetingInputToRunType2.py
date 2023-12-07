"""Copyright(c) 2023 by: duengocnguyen@gmail.com"""
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
from Autodesk.Revit.DB.Structure import *

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
from Autodesk.DesignScript.Geometry import Point


path_to_check = r'C:\Users\NGUYEN NGOC DUE\AppData\Roaming\Dynamo\Dynamo Revit\2.10\packages\packages\BIM3DM\lib'
import sys
sys.path.append(path_to_check)
import BIM3DM
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
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
app  = uidoc.Application
DB = Autodesk.Revit.DB
############################### FUNCTION #################################
def setLayoutAsMinimumClearSpacingForRebar(rebar, spacing, arrayLength, barsOnNormalSide=True, inclFirstBar=True, inclLastBar=True):
    TransactionManager.Instance.EnsureInTransaction(doc)
    rebar = UnwrapElement(rebar)
    re = rebar.GetShapeDrivenAccessor()
    re.SetLayoutAsMinimumClearSpacing(spacing,arrayLength,barsOnNormalSide,inclFirstBar,inclLastBar)
    TransactionManager.Instance.TransactionTaskDone()
    return rebar

############################### INPUT #################################
objects = UnwrapElement(IN[0])
spacing = IN[1]
arrayLength = IN[2]
barsOnNormalSide = IN[3]
inclFirstBar = IN[4]
inclLastBar = IN[5]
# Convert from mm to feet:
if IN[6]:
    spacing = spacing / 304.8
    arrayLength = arrayLength / 304.8
    
allVariable = [objects, spacing, arrayLength,barsOnNormalSide, inclFirstBar, inclLastBar]


############################### OUTPUT ##################################
rank = get_array_rank(objects)
if rank == 0:  # a
    OUT = setLayoutAsMinimumClearSpacingForRebar(*allVariable)
elif rank == 1:  # [a]
    OUT = [setLayoutAsMinimumClearSpacingForRebar(element, *allVariable) for element in objects]
elif rank == 2:  # [[a]]
    OUT = [setLayoutAsMinimumClearSpacingForRebar(i, *allVariable) for j in objects for i in j]
else:
    elements = flatten_to_1d(objects)  # [a]
    OUT = setLayoutAsMinimumClearSpacingForRebar(elements,*allVariable )

