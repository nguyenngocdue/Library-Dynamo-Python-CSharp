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

doc = DocumentManager.Instance.CurrentDBDocument

textnotes = UnwrapElement(IN[1])
View = doc.ActiveView

boundingbox = []

for note in textnotes:
    boundingbox.append(note.get_BounddingBox(View).ToProtoType())

OUT = boundingbox
