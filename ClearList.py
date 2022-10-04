#Copyright(c) 2015, Konrad K Sobon
# @arch_laboratory, http://archi-lab.net

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#The inputs to this node will be stored as a list in the IN variable.
dataEnteringNode = IN

def ClearList(_list):
    out = []
    for _list1 in _list:
        if _list1 is None:
            continue
        if isinstance(_list1, list):
             _list1 = ClearList(_list1)
             if not _list1:
                 continue
        out.append(_list1)
    return out

#Assign your output to the OUT variable
OUT = ClearList(IN[0])