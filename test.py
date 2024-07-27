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
from  Autodesk.Revit.UI.Selection import*
from  Autodesk.Revit.UI.Selection import ISelectionFilter

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
from Autodesk.Revit.DB import Line, ModelLine, LinePattern, ElementId
import Autodesk.Revit.DB as RDB
from Autodesk.Revit.DB import Line, GeometryInstance, Solid

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
app  = uidoc.Application 
# #############################################################
# #                      FUNCTION                             #
def sortXYZ(lstXyz):
    # Sort lstXyz by coordinates X, then Y, then Z
    sortedIndices = sorted(enumerate(lstXyz), key=lambda point: (point[1][0], point[1][1], point[1][2]))
    indices = [index for index, _ in sortedIndices]
    sortedPoints = [point for _, point in sortedIndices]
    return indices, sortedPoints

# #############################################################
# #                      GEOMETRY                             #
# #############################################################

elements = UnwrapElement(IN[1]) if isinstance(IN[1], list) else [UnwrapElement(IN[1])]
OUT = sortXYZ(elements)