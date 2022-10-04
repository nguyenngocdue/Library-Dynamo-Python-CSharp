import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getLevelFloor(SystemFamily):
    ProcessLists = lambda function, lists: [ProcessLists(function, item) if isinstance(item, list) else function(item) for item in lists]
    def Unwrap(item):
        return UnwrapElement(item)
        
    if isinstance(SystemFamily, list):
        items = ProcessLists(Unwrap, SystemFamily)
    else:
        items = Unwrap(SystemFamily)
    level = []
    elevation = []
    for i in items:
        out = i.Document.GetElement(i.get_Parameter(BuiltInParameter.LEVEL_PARAM).AsElementId())
        elevation.append(out.Elevation*304.8)
        level.append(out)
    return level,elevation
OUT = getLevelFloor(IN[0])
