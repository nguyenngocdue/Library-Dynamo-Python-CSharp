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
def flatten_to_minimum_level(lst, level):
    def flatten_helper(items, curr_level):
        flattened = []
        for item in items:
            if curr_level < level and isinstance(item, list):
                flattened.extend(flatten_helper(item, curr_level + 1))
            else:
                flattened.append(item)
        return flattened

    return flatten_helper(lst, 1)
    

def traverse_nested_list(IN):
    def traverse_helper(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(traverse_helper(item))
            elif hasattr(item, 'ToPoint') :
                result.append(item.ToPoint())
            elif hasattr(item, 'ToProtoType'):
            	result.append(item.ToProtoType())
            else:
                result.append(item)
        return result

    return traverse_helper(IN)

object = IN[0]
element = flatten_to_minimum_level(object,100)
OUT =traverse_nested_list(element)