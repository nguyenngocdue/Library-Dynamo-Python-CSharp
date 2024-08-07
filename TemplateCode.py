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
def returnOUT(fn):
	rank = get_array_rank(objects)
	if rank == 1: #a
		return fn
	elif rank == 2: #[a]
		return [fn for element in objects]
	elif rank == 3: #[[a]]
		return [fn for j in objects for i in j]
	else:
		elements = flatten_to_1d(objects) #[a]
		return fn
	return None


#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
app  = uidoc.Application 
###############################CODE HERE#################################
#public
def sortPointsByAxis(points, axis='X', descending=False):
    # Define a lambda function to extract the specified axis value from a point
    key_function = lambda point: getattr(point, axis)
    # Sort the points based on the specified axis
    sorted_points = sorted(points, key=key_function, reverse=descending)
    return sorted_points


objects = IN[1]
descending = IN[2]
axis = IN[3]
#change name of your def
fn = sortPointsByAxis(objects,axis, descending)

###############################END CODE##################################
OUT = returnOUT(fn) 
