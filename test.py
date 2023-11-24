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
clr.AddReference('System.Windows.Forms.DataVisualization')
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

#public
def is_array(obj):
    return "List" in obj.__class__.__name__
#public
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


def filterElementsByGeometryType(elements, typeName='Line'):
    result = []
    if typeName == 'Solid': typeName = 'Mesh'
    for element in elements:
        element = UnwrapElement(element)
        try:
            if(str(element.ToRevitType()).Contains(typeName)):
                result.append(element)
        except:
            continue

    return result

objects = UnwrapElement(IN[1])
typeName = IN[2]

rank = get_array_rank(objects)
if rank == 1:
    OUT = filterElementsByGeometryType(objects, typeName)
elif rank == 2:
    out = []
    for element in objects: out.append(filterElementsByGeometryType(element, typeName))
    OUT = out
else:
    elements = flatten_to_1d(objects)
    OUT = filterElementsByGeometryType(elements, typeName)
