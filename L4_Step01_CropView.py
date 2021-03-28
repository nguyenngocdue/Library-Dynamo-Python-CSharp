import clr
import System

from System.Collections.Generic import*

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import*

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import*

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)


clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

def Distance(p,plane):
    q = p - plane.Origin
    return plane.Normal.DotProduct(q) # chiếu lên q

def ProjectOntoPlane(pts,plane):
    d = Distance(pts,plane)
    p = pts - d*plane.Normal
    return p



pickBox = uidoc.Selection.PickBox(Autodesk.Revit.UI.Selection.PickBoxStyle.Directional,"Please PickBox")

ptsMax = pickBox.Max
ptsMin = pickBox.Min

cropShape = view.GetCropRegionShapeManager()

ptsCheckMax = ptsMax.ToPoint()
ptsCheckMin = ptsMin.ToPoint()

vectorOfView = view.UpDirection
plane = Autodesk.Revit.DB.Plane.CreateByNormalAndOrigin(vectorOfView,ptsMax)

xyz1 = ProjectOntoPlane(ptsMin,plane)
xyz1Check = xyz1.ToPoint()


plane = Autodesk.Revit.DB.Plane.CreateByNormalAndOrigin(vectorOfView,ptsMin)
xyz2 = ProjectOntoPlane(ptsMax, plane)
xyz2Check = xyz2.ToPoint()

curve = [
    Line.CreateBound(ptsMin,xyz1),
    Line.CreateBound(xyz1,ptsMax),
    Line.CreateBound(ptsMax,xyz2),
    Line.CreateBound(xyz2,ptsMin)
]
curveCheck = []
for i in curve:
    curveCheck.append(i.ToProtoType())

curveloop = CurveLoop.Create(curve)

try:

    TransactionManager.Instance.EnsureInTransaction(doc)
    view.CropBoxActive = True
    view.CropBoxVisible = True
    cropShape.SetCropShape(curveloop)
    TransactionManager.Instance.TransactionTaskDone()
    OUT = True
    pass
except:
    button = TaskDialogCommonButtons.Ok
    TaskDialog.Show('Result','None in View 3D', button)
    OUT = False

#OUT = pickBox, ptsCheckMax, ptsCheckMin
#OUT = xyz1Check , ptsCheckMax, ptsCheckMin, xyz2Check