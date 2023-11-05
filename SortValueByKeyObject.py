"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
import clr 
import System
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
import math
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

################################################################
import math
clr.AddReference("RevitAPIUI")
from  Autodesk.Revit.UI import *


objects = IN[1]
keyValues = IN[2]

def getValueByKeyObject(keys, objects):
    arrKeys, values = [], []
    for k in keys:
        if k in objects.keys():
            arrKeys.append(k)
            val =  str(objects[k])
            if val.isnumeric(): values.append(round(float(val),2))
            else: values.append(str(objects[k]))
    return arrKeys, values

OUT = getValueByKeyObject(keyValues, objects[0])