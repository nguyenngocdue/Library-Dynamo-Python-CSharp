import clr
import System
import math 
from System.Collections.Generic import *

clr.AddReference('ProtoGeometry')
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


def GridsFirstEnd(lstGrids):
	keySelect =[]
	ptsGrids =[]
	for i in lstGrids:
		crv = i.Curve
		ptsGrids.append(crv.GetEndPoint(0).X)

	ptsMaxMin = [max(ptsGrids),min(ptsGrids)]

	for i in lstGrids:
		var = i.Curve
		x = var.GetEndPoint(0).X
		for j in ptsMaxMin:
			if j==x:
				keySelect.append(i)
	return keySelect
def RefArrayFromGrids(listGrids,doc):
	refArray = ReferenceArray()
	#dùng để phân tích hình học.
	opt = Options()
	opt.ComputeReferences= True#Xác định xem các tham chiếu đến các đối tượng hình học có được tính toán hay không.
	opt.IncludeNonVisibleObjects = True#Có trích xuất các đối tượng hình học phần tử ẩn không
	opt.View = doc.ActiveView#Khung nhìn được sử dụng để trích xuất hình học.
	for i in elSelect:
		crv = i.Curve
		for j in i.get_Geometry(opt):
			if isinstance(j,Line):
				grRef = j.Reference
				refArray.Append(grRef)
	return refArray
def CurveFromGrids(listGrids,doc):
	crv = []
	#dùng để phân tích hình học.
	opt = Options()
	opt.ComputeReferences= True#Xác định xem các tham chiếu đến các đối tượng hình học có được tính toán hay không.
	opt.IncludeNonVisibleObjects = True#Có trích xuất các đối tượng hình học phần tử ẩn không
	opt.View = doc.ActiveView#Khung nhìn được sử dụng để trích xuất hình học.
	for i in elSelect:
		cr = i.Curve
		crv.append(cr)
	return crv
def OffsetPoint (line,distance):
	base =XYZ.BasisZ
	sp = line.GetEndPoint(0)
	ep = line.GetEndPoint(1)
	vt = (sp+ep).CrossProduct(base).Normalize()
	pstnew = sp+distance*vt
	return vt
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
def GetGeoElement(element): # Get geometry of element.
    geo = []
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.DetailLevel = ViewDetailLevel.Fine
    geoByElement = element.get_Geometry(opt)
    geo = [i for i in geoByElement]
    return geo
def GetSolidFromGeo(lstGeo): # Get Solid from Geo
    sol = []
    for i in lstGeo:
        if i.GetType()== Solid and i.Volume > 0:
            sol.append(i)
        elif i.GetType() == GeometryInstance:
            var = i.SymbolGeometry
            for j in var:
                if j.Volume > 0:
                    sol.append(j)
    return sol
def GetPlanarFormSolid(solids): # Get Planarface from solids
    plaf = []
    for i in solids:
        var = i.Faces
        for j in var:
            if j.Reference != None:
                plaf.append(j)
    return plaf
def Isparalel(p,q):
    return p.CrossProduct(q).IsZeroLength()
def RemoveFaceNone(lstplanars): # Get planarFaces Not Null Value
    pfaces = []
    for i in lstplanars:
        if i.Reference != None:
            pfaces.append(i)
    return pfaces
def GetFaceVertical(plannar): # Get Vertical PlannarFaces 
    re = []
    remove = RemoveFaceNone(plannar)
    for i in remove:
        var = i.FaceNormal
        rad = var.AngleTo(XYZ.BasisZ)
        if 30<(rad*180/3.14)<170:
            re.append(i)
    return re
def GetTopOrBotFace(lstPlanars, reason): # Get Top or Bottom of Faces
    for i in lstPlanars:
        if i.FaceNormal.Z == 1 and reason == True:
            return i
    for i in lstPlanars:
        if i.FaceNormal.Z == -1 and reason == False:
            return i
def RetrieveEdgesFace(lstPlanar): # Get Lines of PlanarFaces
    re = []
    var = lstPlanar.EdgeLoops
    for i in var:
        for j in i:
            re.append(j.AsCurve())
    return re
def GetLineMax(lstLine): # Get a min line of list line
    _length = []
    lineMax = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == max(_length):
            lineMax.append(j)
    return lineMax
def lstFlattenL1(list): 
    result = []
    for i in list:
        result.append(i)
    return result
def lstFlattenL2(list):
    result = []
    for i in list:
        for j in i:
            result.append(j)
    return result

ele = SelectionFilter("Grids", "Structural Framing")
elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")
elSelect= [elSelectAll[0]]
eleFraming = elSelectAll[1]

#OUT = elSelect

curveCheck =[]

vtxPlane = XYZ.BasisZ
vtxSection = XYZ.BasisY

crvGrids= CurveFromGrids(elSelect,doc)

ptsGris1 = crvGrids[0].GetEndPoint(0)
ptsGris2 = crvGrids[0].GetEndPoint(1)

vtxFromGrids = ptsGris1-ptsGris2

#OUT = line.ToProtoType(), elSelect
refGids = RefArrayFromGrids(elSelect,doc)
pickPoint = uidoc.Selection.PickPoint("Select Point")
direct = vtxPlane.CrossProduct(vtxFromGrids)  # Nhân hai vector (0,0,1)*(0,1,0)=(1,0,0) is line vuông góc với Grids

line = Line.CreateBound(pickPoint,pickPoint+direct)  # Get đường vuông góc với Grid

getGeoFraming = GetGeoElement(eleFraming)
OUT = getGeoFraming

getSolidFraming = GetSolidFromGeo(getGeoFraming)
OUT = [i.ToProtoType() for i in  getSolidFraming]

getPlanarFraming = GetPlanarFormSolid(getSolidFraming)
#OUT = getPlanarFraming

getFaceVertiFraming = GetFaceVertical(getPlanarFraming)
OUT = [i.ToProtoType() for i in getFaceVertiFraming]


getLineVetiFraming = RetrieveEdgesFace(getFaceVertiFraming[0])
OUT = [i.ToProtoType() for i in getLineVetiFraming]
getLongLine = GetLineMax(getLineVetiFraming)
OUT = [i.ToProtoType() for i in getLongLine]

direcFraming = (getLongLine[0].Direction) # Get direction to define for Dimention Offset

def GetReference(lstPlanar):
    re = []
    for i in lstPlanar:
        re.append(i.Reference)
    return re

refVFraming = GetReference(getFaceVertiFraming) # Get 2 reference of 2 vertical faces
allRef = lstFlattenL2([refVFraming,refGids]) # Get all refFraming + refGrids
OUT = allRef

##################################################Framing From Center to Center of Column ###################
re = ReferenceArray()
for i in allRef:
    re.Append(i)

re2 = ReferenceArray()
for i in refVFraming:
    re2.Append(i)
#############################################################################################################


def LineOffset(line,distance,direc1, direc2, Flip): # Offset a line from one line earlier
    convert = distance
    #newVector = None
    vt =XYZ.BasisY
    checkY = Isparalel(vt,direct)
    if checkY == True:
        if direc1 == "x" or "X": dir = Flip*direc2*(1/304.8)*convert
    else:
        if direc1 == "y" or "Y": dir = Flip*direc2*(1/304.8)*convert
    #if direc == "z" or "Z": newVector = XYZ(0,0,convert)
    trans = Transform.CreateTranslation(dir) # Setting direction for GetLinMin
    lineMove = line.CreateTransformed(trans)
    return lineMove

offsetline =LineOffset(line,IN[1],"X",direcFraming, IN[2] )
OUT = line.ToProtoType() ,offsetline.ToProtoType(), direct

##############################################################################################################
# Explain when it has 4 faces vertical
def GetMaxface(plananrs):
    _Area = []
    _face = []
    for i in plananrs:
        _Area.append(i.Area)
    for j in plananrs:
        if j.Area > 10:
            _face.append(j)
            
    return _face
getMaxFaceVFraming = GetMaxface(getFaceVertiFraming)
OUT = getMaxFaceVFraming

refVFraming02 = GetReference(getMaxFaceVFraming)
allRef02 = lstFlattenL2([refVFraming02,refGids])
OUT = allRef02

re02 = ReferenceArray()
for i in allRef02:
    re02.Append(i)

re03 = ReferenceArray()
for i in refVFraming02:
    re03.Append(i)


#################################################Dimensions#####################################################
TransactionManager.Instance.EnsureInTransaction(doc)

dim1 = doc.Create.NewDimension(view, line, re02)
dim2 =doc.Create.NewDimension(view,offsetline,re03)

TransactionManager.Instance.TransactionTaskDone()


#OUT = direcFraming , line.ToProtoType() , offsetline.ToProtoType() 
###############################################################################################################

OUT = direct , line.ToProtoType(), vtxFromGrids , ptsGris1, ptsGris2