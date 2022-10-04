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
def lstFlattenL1(list): #List.Flatten
    result = []
    for i in list:
        result.append(i)
    return result
def lstFlattenL2(list): #List.Flatten
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
def RemoveFaceNone(lstplanars): # Get planarFaces Not Null Value
    pfaces = []
    for i in lstplanars:
        if i.Reference != None:
            pfaces.append(i)
    return pfaces
def Isparalel(p,q):
    return p.CrossProduct(q).IsZeroLength()
def GetFaceVertical(plannar): # Get Vertical PlannarFaces 
    re = []
    remove = RemoveFaceNone(plannar)
    for i in remove:
        var = i.FaceNormal
        rad = var.AngleTo(XYZ.BasisZ)
        if 30<(rad*180/3.14)<170:
            re.append(i)
    return re
def GetMaxface(plananrs):
    _Area = []
    _face = []
    for i in plananrs:
        _Area.append(i.Area)
    for j in plananrs:
        if j.Area > (max(_Area)-min(_Area)):
            _face.append(j)
            
    return _face

def GetReference(lstPlanar):
    reArray = []
    for i in lstPlanar:
        re = []
        for j in i:
            re.append(j.Reference)
        reArray.append(re)
    return reArray
def GetRefArrayOfGetRefer(lstRefer):
    reArray = ReferenceArray()
    for i in lstRefer:
        re = []
        for j in i:
            re.append(j)
        for t in re:
            reArray.Append(t)
    return reArray

def ReferenceFromSurface(ElementSurface): # Get Revit.DB.Reference from Surface
    ref = []
    for i in ElementSurface:
        re =[]
        for j in i:
            re.append(j.Tags.LookupTag("RevitFaceReference"))
        ref.append(re)
    return ref
def chunks(l, n): #List.Chop
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def LinebyGrids(lstGrids):
    re = []
    for i in lstGrids:
        crv = i.Curve
        re.append(crv.ToProtoType())
    return re
def DBLinebyGrids(lstGrids):
    re = []
    for i in lstGrids:
        crv = i.Curve
        re.append(crv)
    return re

def Combine_EleSurface_EleCurve_RefGrids(EleCurve,EleSurface,RefGrids): # Combine Ref's Surface and Ref
    Ref=[]
    for i in range(0,len(EleSurface)):
        dis =[]
        for j in EleSurface[i]:
            dis.append(EleCurve[i].DistanceTo(j))
        if dis[0] !=0 and dis[1] !=0:
            #su[i].insert(0,lst[i])
            EleSurface[i].insert(0,RefGrids[i])
            
    for i in range(0,len(EleSurface)):
        re =[]
        for j in EleSurface[i]:
            if str(j).Contains('Surface'):
                re.append(j.Tags.LookupTag("RevitFaceReference"))
            else:
                re.append(j)
        Ref.append(re)
    return Ref


ele = SelectionFilter("Grids", "Structural Framing")
elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")

fls = FilteredElementCollector(doc, view.Id).ToElements()
AllEle = elSelectAll
grids = []
eleFraming = []
for i in AllEle:
    try:
        if i.Category.Name == "Grids":
            grids.append(i)
        if i.Category.Name == "Structural Framing":
            eleFraming.append(i)
    except:
        pass
OUT = AllEle, grids,eleFraming

refOfGrids = GetReferenceOfGrid(grids)
OUT = refOfGrids

getLineGrids = LinebyGrids(grids)

getGeoFraming = [GetGeoElement(i) for i in eleFraming]
OUT = getGeoFraming

getSolidFraming = [GetSolidFromGeo(i) for i in getGeoFraming]
OUT = getSolidFraming

getFaceFraming = [GetPlanarFormSolid(i) for i in getSolidFraming]
OUT = getFaceFraming

getFaVerFraming = [GetFaceVertical(i) for i in getFaceFraming]
OUT = getFaVerFraming

getFaMaxVerFraming = [GetMaxface(i) for i in getFaVerFraming]
OUT = getFaMaxVerFraming
eleSurface = lstFlattenL2([j.ToProtoType() for i in getFaMaxVerFraming for j in i])
eleSurface = chunks(eleSurface,2)
OUT =eleSurface,refOfGrids,getLineGrids

getLineDirec = DBLinebyGrids(grids)[0]

ptsLine1 = getLineDirec.GetEndPoint(0)
ptsLine2 = getLineDirec.GetEndPoint(1)

vtyFromLine = ptsLine1 - ptsLine2
vtzPlane = XYZ.BasisZ
pickPoint = uidoc.Selection.PickPoint("Select Point")
direct = vtzPlane.CrossProduct(vtyFromLine) 
line = Line.CreateBound(pickPoint,pickPoint+direct)

def LineOffset(line,distance,direc1, direc2, Flip): # Offset a line from one line earlier
    convert = distance/304.8
    #newVector = None
    vt =XYZ.BasisY
    checkY = Isparalel(vt,direct)
    if checkY == True:
        if direc1 == "x" or "X": dir = Flip*direc2*convert
    else:
        if direc1 == "y" or "Y": dir = Flip*direc2*convert
    #if direc == "z" or "Z": newVector = XYZ(0,0,convert)
    trans = Transform.CreateTranslation(dir) # Setting direction for GetLinMin
    lineMove = line.CreateTransformed(trans)
    return lineMove

directline = getLineDirec.Direction 

offsetline =LineOffset(line,IN[1],"Y",directline,IN[2])

OUT = line, eleSurface,refOfGrids,getLineGrids,offsetline
#OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK