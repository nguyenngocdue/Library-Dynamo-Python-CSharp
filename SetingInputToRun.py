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

#from lib import framework

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


def get_gridpoints(grids):
    source_grids = grids
    
    return [GridPoint(point=k, grids=v) for k, v in gints.items()]

###############################INPUT#################################
objects = UnwrapElement(IN[1])

###############################OUTPUT##################################
rank = get_array_rank(objects)
if rank == 1: #a
    OUT = get_gridpoints(objects)
elif rank == 2: #[a]
    OUT = [get_gridpoints(element) for element in objects]
elif rank == 3: #[[a]]
    OUT = [get_gridpoints(i) for j in objects for i in j]
else:
    elements = flatten_to_1d(objects) #[a]
    OUT =  get_gridpoints(elements)