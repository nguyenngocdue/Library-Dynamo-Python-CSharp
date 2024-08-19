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
from Autodesk.DesignScript.Geometry import Line
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument


#########################################################################

doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#########################################################################

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import PolyCurve, Line

def createClosedPolyCurve(points):
    # Tạo PolyCurve từ danh sách các điểm
    lines = [Line.ByStartPointEndPoint(points[i], points[(i + 1) % len(points)]) for i in range(len(points))]
    polyCurve = PolyCurve.ByJoinedCurves(lines)
    
    # Đóng PolyCurve nếu nó chưa khép kín
    if not polyCurve.IsClosed:
        polyCurve = polyCurve.Close()

    return polyCurve

# Giả sử points là danh sách các điểm XYZ bạn có
# Đoạn code giả sử IN[0] là danh sách các điểm
points = IN[0]
OUT = createClosedPolyCurve(points)
