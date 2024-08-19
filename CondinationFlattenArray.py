"""Copyright(c) 2023 by: duengocnguyen@gmail.com"""
"site_url: https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g",
"repository_url:https://github.com/nguyenngocdue/Library-Dynamo-Python-CSharp"
"""________________Welcome to BIM3DM-DYNAMO API___________________"""

import clr
import System
 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import*
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import Selection
from  Autodesk.Revit.UI.Selection import ISelectionFilter

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
#########################################################################
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
# clr.AddReference('System.Windows.Forms.DataVisualization')
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
from Autodesk.Revit.DB import Line, Solid, Arc
#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
#View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

#########################################################################


#########################################################################

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

def is_array(obj):
    return "List" in obj.__class__.__name__

def get_array_rank(array):
    if is_array(array):
        return 1 + max(get_array_rank(item) for item in array)
    else:
        return 0

def flatten_array_more_then_num(objects, level):
    result = []
    for item in objects:
        newRank = get_array_rank(item)
        if  is_array(item) and newRank >= level:
            arr = flatten_to_1d(item)
            result.append(arr)
        else:
            result.append(item)
    return result

objects = UnwrapElement(IN[1])
OUT = flatten_array_more_then_num(objects, 2)
