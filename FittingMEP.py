import clr
import math
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# Lấy ống và điểm từ input hoặc bằng cách tìm trong dự án Revit
pipe = UnwrapElement(IN[0])
point = UnwrapElement(IN[1])
fitting_type = UnwrapElement(IN[2])

def CreateMEPFittingByPointsAndCurve(fitting_type, point, pipe):
    doc = DocumentManager.Instance.CurrentDBDocument
    
    TransactionManager.Instance.EnsureInTransaction(doc)

    fitting = doc.Create.NewFamilyInstance(point, fitting_type, pipe, Structure.StructuralType.NonStructural)
    
    TransactionManager.Instance.TransactionTaskDone()

    return fitting

# Chuyển đổi điểm từ feet sang mm
point = XYZ(point.X / 304.8, point.Y / 304.8, point.Z / 304.8)

OUT = CreateMEPFittingByPointsAndCurve(fitting_type, point, pipe)
