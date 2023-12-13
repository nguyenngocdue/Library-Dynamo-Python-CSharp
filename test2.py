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
objects = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
params = UnwrapElement(IN[1]) if isinstance(IN[1],list) else [UnwrapElement(IN[1])]
values = UnwrapElement(IN[2]) if isinstance(IN[2],list) else [UnwrapElement(IN[2])]


def setValueByName(_paramDB, nameToCheck, values, i):
	if hasattr(_paramDB, "Definition"):
		TransactionManager.Instance.EnsureInTransaction(doc)
		if _paramDB.Definition.Name == nameToCheck:
			if _paramDB.StorageType == StorageType.Double:
				_paramDB.Set(values[i]/304.84)
				return True
			elif _paramDB.StorageType == StorageType.ElementId:
				_paramDB.Set(values[i].Id)
				return True
			else:
				_paramDB.Set(str(values[i]))
				return True
		TransactionManager.Instance.TransactionTaskDone()
	else:
		return False

def setParameterByNames(items,params,values):
	for i,paramName in enumerate(params):
		for elem in items:
			TransactionManager.Instance.TransactionTaskDone()
			paramDB =  elem.LookupParameter(paramName)
			hasValue = setValueByName(paramDB, paramName, values, i)
			if not hasValue:
				familyType = doc.GetElement(elem.GetTypeId())
				allParams = familyType.Parameters
				for paramDB2 in allParams:
					hasValue2 = setValueByName(paramDB2, paramName, values, i)
	return items



allVariable = [params,values]
############################### OUTPUT ##################################
rank = get_array_rank(objects)
rank2 = get_array_rank(values)
objects = objects if rank else [objects]
values = values if rank2 else [values]
if rank == 1:  # a
    OUT = setParameterByNames(objects,*allVariable)
elif rank == 2:  # [a]
    OUT = [setParameterByNames(element, *allVariable) for element in objects]
elif rank == 3:  # [[a]]
    OUT = [setParameterByNames(i, *allVariable) for j in objects for i in j]
else:
    elements = flatten_to_1d(objects)  # [a]
    OUT = setParameterByNames(elements,*allVariable )
