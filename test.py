import clr 
import System
import math 
from System.Collections.Generic import *


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

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#########################################################################
def unwrapInput(inputValue):
    if isinstance(inputValue, list):
        return UnwrapElement(inputValue)
    else:
        return [UnwrapElement(inputValue)]



def checkAxisMovement(points):
    # Assume the list contains at least two points to compare
    if len(points) < 2:
        return "Not enough points to check."

    # Get the coordinates of the first and second points, rounding to 4 decimal places
    x1, y1, z1 = round(points[0].X, 4), round(points[0].Y, 4), round(points[0].Z, 4)
    x2, y2, z2 = round(points[1].X, 4), round(points[1].Y, 4), round(points[1].Z, 4)

    # Check the differences in the rounded coordinates
    if x1 != x2 and y1 == y2 and z1 == z2:
        return "X"
    elif x1 == x2 and y1 != y2 and z1 == z2:
        return "Y"
    elif x1 == x2 and y1 == y2 and z1 != z2:
        return "Z"
    else:
        return "Movement along multiple axes or no clear axis of movement."

# Apply the function to the list of elements
elements = unwrapInput(IN[1])
OUT = checkAxisMovement(elements)
