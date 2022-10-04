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

class SelectionFilter(ISelectionFilter):
	def __init__(self, ctgName1 , ctgName2):
		self.ctgName1 = ctgName1
		self.ctgName2 = ctgName2

	def AllowElement(self, element):
		if element.Category.Name == self.ctgName1 or element.Category.Name == self.ctgName2:
			return True
		else:
			return False
	def AllowReference(ref, xyZ):
		return False

def GetReferenceOfGrid(ElementGrids): # Get Revit.DB.Reference from Grids
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    refGrids = []
    for i in UnwrapElement(ElementGrids):
        f = (i.get_Geometry(opt))
        [refGrids.append(j.Reference) for j in f if str(j).Contains("Line")]
    return refGrids

def CurveFromGrids(listGrids,doc):
	crv = []
	#dùng để phân tích hình học.
	opt = Options()
	opt.ComputeReferences= True#Xác định xem các tham chiếu đến các đối tượng hình học có được tính toán hay không.
	opt.IncludeNonVisibleObjects = True#Có trích xuất các đối tượng hình học phần tử ẩn không
	opt.View = doc.ActiveView#Khung nhìn được sử dụng để trích xuất hình học.
	for i in grids:
		cr = i.Curve
		crv.append(cr)
	return crv

def RefArrayFormRef(reference):
    re  = ReferenceArray()
    for i in reference:
        re.Append(i)
    return re


###--------------------------------------- Step 1 -------------------------------###

ele = SelectionFilter("Grids", "Lines")
elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")
OUT = elSelectAll

###--------------------------------------- Step 2 -------------------------------###

lines = []
grids = []
for i in elSelectAll:
    if i.Category.Name == "Lines": lines.append(i)
    if i.Category.Name == "Grids": grids.append(i)
OUT =  lines, grids
refAllEle = GetReferenceOfGrid(elSelectAll)

###--------------------------------------- Step 3 -------------------------------###
### Snap Point
getline = (CurveFromGrids(grids, doc))[0]

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
refArrsy = RefArrayFormRef(refAllEle)

TransactionManager.Instance.EnsureInTransaction(doc)

dim1 = doc.Create.NewDimension(view, line,refArrsy )

TransactionManager.Instance.TransactionTaskDone()
