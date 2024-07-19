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
def getRefArrayFromDBLine(grids,doc):
    refArray = ReferenceArray()   
    for j in grids:
        refArray.Append(j.Reference)
    return refArray
# #############################################################

# #############################################################
# #                      GEOMETRY                             #
# #############################################################

dbLine = IN[1]
grids = IN[2]

TransactionManager.Instance.EnsureInTransaction(doc)
refs = getRefArrayFromDBLine(grids, doc)
dim = doc.Create.NewDimension(view, dbLine, refs)
TransactionManager.Instance.TransactionTaskDone()
OUT = dim