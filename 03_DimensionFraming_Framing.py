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
def getGeoElement(element): # Get geometry of element.
    geo = []
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.DetailLevel = ViewDetailLevel.Fine
    geoByElement = element.get_Geometry(opt)
    geo = [i for i in geoByElement]
    return geo
def getSolidFromGeo(lstGeo): # Get Solid from Geo
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
def getPlanarFormSolid(solids): # Get Planarface from solids
    plaf = []
    for i in solids:
        var = i.Faces
        for j in var:
            if j.Reference != None:
                plaf.append(j)
    return plaf
def getMaxface(plananrs):
    _Area = []
    _face = []
    for i in plananrs:
        _Area.append(i.Area)
    for j in plananrs:
        if j.Area > (max(_Area)-min(_Area)):
            _face.append(j)
    return _face
def RemoveFaceNone(dbPlanarFaces): # Get planarFaces Not Null Value
    pfaces = []
    for i in dbPlanarFaces:
        if i.Reference != None:
            pfaces.append(i)
    return pfaces
def getFaceVertical(plannar): # Get Vertical PlanarFaces 
    re = []
    remove = RemoveFaceNone(plannar)
    for i in remove:
        var = i.FaceNormal
        rad = var.AngleTo(XYZ.BasisZ)
        if 30<(rad*180/3.14)<170:
            re.append(i)
    return re
def RetrieveEdgesFace(lstPlanar): # Get Lines of PlanarFaces
    re = []
    var = lstPlanar.EdgeLoops
    for i in var:
        for j in i:
            re.append(j.AsCurve())
    return re
def getLineMax(lstLine): # Get a min line of list line
    _length = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == max(_length):
            return j   
def chunks(l, n): #List.Chop
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def ReferenceFromSurface(ElementSurface): # Get Revit.DB.Reference from Surface
    ref = []
    for i in ElementSurface:
        re =[]
        for j in i:
            re.append(j.Tags.LookupTag("RevitFaceReference"))
        ref.append(re)
    return ref
    #OUT = ReferenceFromSurface(UnwrapElement(IN[1]))
def getReferenceArray(lstPlanar):
    reArray = ReferenceArray()
    for i in lstPlanar:
        reArray.Append(i.Reference)
    return reArray

ele = SelectionFilter("NOT", "Structural Framing")
elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")
elSelect= [elSelectAll[0]]
eleFraming = elSelectAll

OUT = eleFraming

getGeoFraming = [GetGeoElement(i) for i in eleFraming]
OUT = getGeoFraming
getSolidFraming = [GetSolidFromGeo(i) for i in getGeoFraming]
OUT = getSolidFraming
getFaceFraming = [GetPlanarFormSolid(i) for i in getSolidFraming]
OUT = getFaceFraming
getFaMaxVerFraming = [GetMaxface(i) for i in getFaceFraming]
OUT = getFaMaxVerFraming
getFaVerFraming = [GetFaceVertical(i) for i in getFaMaxVerFraming]
OUT = getFaVerFraming
GetLineFraming = RetrieveEdgesFace(getFaVerFraming[0][0])
OUT = GetLineFraming
GetLineMax = GetLineMax(GetLineFraming)
OUT = GetLineMax

##################################################
vtxPlane = XYZ.BasisZ
vtxSection = XYZ.BasisY

ptsLine1 = GetLineMax.GetEndPoint(0)
ptsLine2 = GetLineMax.GetEndPoint(1)

vtxFromLine = ptsLine1 - ptsLine2

pickPoint = uidoc.Selection.PickPoint("Select Point")
direct = vtxPlane.CrossProduct(vtxFromLine) 
line = Line.CreateBound(pickPoint,pickPoint+direct)
###################################################
refFace =[GetReferenceArray(i) for i in getFaVerFraming]




TransactionManager.Instance.EnsureInTransaction(doc)

dim = doc.Create.NewDimension(view, line, refFace)

TransactionManager.Instance.TransactionTaskDone()









