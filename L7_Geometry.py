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
def getPlanarsFromSolids(solids): # Get Planarface from solids
    pls = []
    for solid in solids: 
        faces = solid.Faces
        return [pl for pl in faces if pl.Reference]
def RemoveFaceNone(dbPlanarFaces): # Get planarFaces Not Null Value
    pfaces = []
    for i in dbPlanarFaces:
        if i.Reference != None:
            pfaces.append(i)
    return pfaces
def Isparalel(p,q):
    return p.CrossProduct(q).IsZeroLength()
def getVerticalPlanars(planars): # Get Vertical PlanarFaces 
    pls = []
    x = XYZ.BasisX
    y = XYZ.BasisY
    for planar in planars:
        faNomal = planar.FaceNormal
        isparalelX  = Isparalel(x,faNomal)
        isparalelY  = Isparalel(y,faNomal)
        if isparalelX == True or isparalelY == True:
            pls.append(planar)
    return pls
def FilterHorizontalPlanar(lstPlface): # Get Horizaontal PlanarFaces 
    faH = []
    z = XYZ.BasisZ
    for i in lstPlface:
        check = Isparalel(z, i.FaceNormal)
        if check == True:
            faH.append(i)
    return faH
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
def getFaceVertical(plannar): # Get Vertical PlanarFaces 
    re = []
    remove = RemoveFaceNone(plannar)
    for i in remove:
        var = i.FaceNormal
        rad = var.AngleTo(XYZ.BasisZ)
        if 30<(rad*180/3.14)<170:
            re.append(i)
    return re
def getRightDbPlanarFaces(dbPlanarFaces,activeView): # Get Right PlanarFaces of a Element
    direct = view.RightDirection
    for i in dbPlanarFaces:
        var = i.FaceNormal
        if var.IsAlmostEqualTo(direct):
            return i
def getLeftDbPlanarFaces(dbPlanarFaces,activeView): # Get Right PlanarFaces of a Element
    direct = view.RightDirection
    for i in dbPlanarFaces:
        var = -1*i.FaceNormal
        if var.IsAlmostEqualTo(direct):
            return i
def getRightOrLeft(dbPlanarFaces,reason,activeView): # Choose in one of Right and Left of Faces
    if reason == True: return getRightDbPlanarFaces(dbPlanarFaces,activeView)
    elif reason == False: return getLeftDbPlanarFaces(dbPlanarFaces, activeView)

fls = FilteredElementCollector(doc, view.Id).ToElements()
AllEle = []
rebars = []
eleFloors = []
eleFraming = []

for i in fls:
    try:
        if i.Category.Name == "Structural Framing":
            eleFraming.append(i)
        if i.Category.Name == "Floors":
            eleFloors.append(i)
        if i.Category.Name == "Structural Framing" or i.Category.Name == "Floors":
            AllEle.append(i)
        if i.Category.Name == "Structural Rebar":
            rebars.append(i)
    except:
        pass
#OUT = AllEle, rebars , eleFloors , eleFraming

getGeoFraming = [GetGeoElement(i) for i in eleFraming]
getGeoFloors = [GetGeoElement(i) for i in eleFloors]
getGeoAllEle = [GetGeoElement(i) for i in AllEle]
#OUT = getGeoFraming, getGeoFloors , getGeoAllEle

getSolidFraming = [GetSolidFromGeo(i) for i in getGeoFraming]
getSolidFloors = [GetSolidFromGeo(i) for i in getGeoFloors]
getSolidAllEle = [GetSolidFromGeo(i) for i in getGeoAllEle]
#OUT = getSolidFraming, getSolidFloors , getSolidAllEle

getFaceFraming = [GetPlanarFormSolid(i) for i in getSolidFraming]
getFaceFloors = [GetPlanarFormSolid(i) for i in getSolidFloors]
getFaceAllEle = [GetPlanarFormSolid(i) for i in getSolidAllEle]
#OUT = getFaceFraming, getFaceFloors, getFaceFloors

getFaHoriFraming = [FilterHorizontalPlanar(i) for i in getFaceFraming]
getFaHoriFloor = [FilterHorizontalPlanar(i) for i in getFaceFloors]
getFaHoriAllEle = [FilterHorizontalPlanar(i) for i in getFaceAllEle]
#OUT = getFaHoriFraming , getFaHoriFloor, getFaHoriAllEle

getFaVerFraming = [FilterVerticalPlanar(i) for i in getFaceFraming]
getFaVerFloors = [FilterVerticalPlanar(i) for i in getFaceFloors]
getFaVerAllEle = [FilterVerticalPlanar(i) for i in getFaceAllEle]

#ChooseFace  = GetRightOrLeft(listFlattenL2(getFaceFraming),view)
#OUT =  ChooseFace.ToProtoType()

faceFraming = [i.ToProtoType() for i in lstFlattenL2(getFaceFraming)]
angle = GetFaceVertical(lstFlattenL2(getFaceFraming))
#OUT = faceFraming,angle

faceV = GetFaceVertical(lstFlattenL2(getFaceFraming))
checkfaceV = [i.ToProtoType() for i in lstFlattenL2(getFaceFraming)]
OUT = faceV, checkfaceV