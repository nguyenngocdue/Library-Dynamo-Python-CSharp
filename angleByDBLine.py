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

dbLine1 = UnwrapElement(IN[0])
dbLine2 = UnwrapElement(IN[1])
num = IN[2]


def calculate_angle(dbLine1, dbLine2):
    # Get the end points of dbLine1
    pts1Line = [dbLine1.GetEndPoint(0), dbLine1.GetEndPoint(1)]
    # Get the end points of dbLine2
    pts2Line = [dbLine2.GetEndPoint(0), dbLine2.GetEndPoint(1)]
    # Sort the end points based on X coordinate
    pts1Line.sort(key=lambda pt: pt.X)
    pts2Line.sort(key=lambda pt: pt.X)
    # Calculate vector direction of line 1
    vector1 = pts1Line[1] - pts1Line[0]
    # Calculate vector direction of line 2
    vector2 = pts2Line[1] - pts2Line[0]
    # Calculate dot product of the two vectors
    dot_product = vector1.DotProduct(vector2)
    # Calculate magnitudes of the two vectors
    magnitude1 = vector1.GetLength()
    magnitude2 = vector2.GetLength()
    # Calculate cos(theta) using dot product / (magnitude1 * magnitude2)
    cos_theta = dot_product / (magnitude1 * magnitude2)
    # Calculate the angle between the two lines in radians
    angle_rad = math.acos(cos_theta)
    # Convert the angle from radians to degrees
    angle_deg = math.degrees(angle_rad)
    return angle_deg
angle = calculate_angle(dbLine1[0], dbLine2[0])
if(num > 0):
    angle = 180 - round(angle)
OUT = round(angle)
    

