"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
"site_url: https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g",
"repository_url:https://github.com/nguyenngocdue/Library-Dynamo-Python-CSharp"
"""________________Welcome to BIM3DM-DYNAMO API___________________"""

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

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
def getList(input_element):
    if isinstance(input_element, list):
        # Unwrap each element in the list
        elements = input_element
    else:
        # Unwrap the single element
        elements = [input_element]
    return elements;
##########################################################################
class HorizontalPlanarFaceFilter:
    @staticmethod
    def isParallel(p, q):
        return p.CrossProduct(q).IsZeroLength()
    @classmethod
    def filterFaces(cls, objects, oxyz = XYZ.BasisZ):
        faH = []
        for i in objects:
            if type(i) == Autodesk.Revit.DB.PlanarFace:
                check = cls.isParallel(oxyz, i.FaceNormal)
                if check == True:
                    faH.append(i)
        return faH
    
objects = getList(IN[1])
oxyz = IN[2]
if oxyz == 'x' or oxyz == 'X':
    oxyz = XYZ.BasisX
elif oxyz == 'y' or oxyz == 'Y':
    oxyz = XYZ.BasisY
else:
    oxyz = XYZ.BasisZ
if objects[0][0] is not None:
    OUT = [HorizontalPlanarFaceFilter.filterFaces(i, oxyz) for i in objects]
else:
    OUT = filterHorizontalPlanarFaces(objects)


