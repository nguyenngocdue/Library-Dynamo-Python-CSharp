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

from System.Collections.Generic import*

#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
################################################################
def isolateElements(elements):
    try:
        TransactionManager.Instance.EnsureInTransaction(doc)
        reset = view.DisableTemporaryViewMode(TemporaryViewMode.TemporaryHideIsolate)
        ids = List[ElementId]()
        for i in elements:
            ids.Add(i.Id)
        view.IsolateElementsTemporary(ids)
        return ids
        TransactionManager.Instance.TransactionTaskDone()
    except Exception as e:
        TransactionManager.Instance.ForceCloseTransaction()
        return "An error occurred: " + str(e)

################################################################
selectedEles = UnwrapElement(IN[1])
OUT = isolateElements(selectedEles)
