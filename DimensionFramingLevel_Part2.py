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

import clr
clr.AddReference('DSCoreNodes')
from DSCore import *

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument


getline = IN[1]

###--------------------------------------- Step 4 -------------------------------###

ptsLine1 = getline.GetEndPoint(0)
ptsLine2 = getline.GetEndPoint(1)
vtyFromLine = ptsLine1 - ptsLine2
vtzPlane = XYZ.BasisZ
pickPoint = uidoc.Selection.PickPoint("Select Point")  # Please Set Work Plan not Error
direct = vtzPlane.CrossProduct(vtyFromLine) 
line = Line.CreateBound(pickPoint,pickPoint+direct)
OUT =  line.ToProtoType(), getline.ToProtoType()

###--------------------------------------- Step 5 -------------------------------###

