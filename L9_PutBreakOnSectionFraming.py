import clr
import System

from System.Collections.Generic import*

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import*

clr.AddReference('RevitAPI')
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
def Isparael(p,q):
    return p.CrossProduct(q).IsZeroLength()
def FilterVerticalPlanar(lstPlface): # Get Vertical PlannarFaces 
    faV = []
    x = XYZ.BasisX # You can change that value to have a new direction
    for i in lstPlface:
        faNomal = i.FaceNormal
        check  = Isparalel(x,faNomal)
        if check == True:
            faV.append(i)
    return faV
def FilterHorizontalPlanar(lstPlface): # Get Horizaontal PlannarFaces 
    faH = []
    z = XYZ.BasisZ
    for i in lstPlface:
        check = Isparael(z, i.FaceNormal)
        if check == True:
            faH.append(i)
    return faH
def GetFaceVertical(plannar): # Get Vertical PlannarFaces 
    re = []
    remove = RemoveFaceNone(plannar)
    for i in remove:
        var = i.FaceNormal
        rad = var.AngleTo(XYZ.BasisZ)
        if 30<(rad*180/3.14)<170:
            re.append(i)
    return re
    #getFaVerFraming = [GetFaceVertical(i) for i in getFaceFraming]
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
def GetFaceVertical(plannar): # Get Vertical PlannarFaces 
    re = []
    remove = RemoveFaceNone(plannar)
    for i in remove:
        var = i.FaceNormal
        rad = var.AngleTo(XYZ.BasisZ)
        if 30<(rad*180/3.14)<170:
            re.append(i)
    return re
def RightFace(lstplanar,viewin): # Get Right PlannarFaces of a Element
    direc = view.RightDirection
    for i in lstplanar:
        var = i.FaceNormal
        if var.IsAlmostEqualTo(direc):
            return i
def LeftFace(lstplanar,viewIn): # Get Right PlannarFaces of a Element
    direc = view.RightDirection
    for i in lstplanar:
        var = -1*i.FaceNormal
        if var.IsAlmostEqualTo(direc):
            return i
def GetRightOrLeftFace(lstFace,reason,viewin): # Choose in one of Right and Left of Faces
    if reason == True: return RightFace(lstFace,viewin)
    elif reason == False: return LeftFace(lstFace, viewin)
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
def GetLineMin(lstLine): # Get a min line of list line
    _length = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == min(_length):
            return j   
def LineOffset(line,distance,direc): # Offset a line from one line earlier
    convert = distance/304.8
    if direc == "x" or "X": newVector = XYZ(convert,0,0)
    if direc == "y" or "Y": newVector = XYZ(0,convert,0)
    if direc == "z" or "Z": newVector = XYZ(0,0,convert)
    # newVector = XYZ(convert,0,0)
    # newVector = XYZ(0,0,convert)

    trans = Transform.CreateTranslation(direc) # Setting direction for GetLinMin
    lineMove = line.CreateTransformed(trans)
    return lineMove 
def GetReferenceArray(lstPlanar):
    reArray = ReferenceArray()
    for i in lstPlanar:
        reArray.Append(i.Reference)
    return reArray
def GetLineVertical(lstLine): # Get vertical Line by Isparalel
    re = []
    NorRevit = XYZ.BasisZ
    for i in lstLine:
        NorLo = i.Direction
        if Isparael(NorLo, NorRevit):
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

def GetTopFacesEle(planar):
    re = []
    z =XYZ.BasisX
    remove = RemoveFaceNone(planar)
    for i in remove:
        var = i.FaceNormal
        rad = var.AngleTo(XYZ.BasisZ)
        if (rad*180)/3.14 < 10 :
            re.append(i)
    return re

def GetIntersection(face, line):
    re = []
    results = clr.Reference[IntersectionResultArray]()
    intersect = face.Intersect(line, results)
    if intersect == SetComparisonResult.Overlap:
        var1 = results.Item[0]
        var2 = var1.XYZPoint
        re.append(var2)
    return re

def PointOffset1(lstPoint, dis, face):
    re = []
    if len(lstPoint) > 1:
        ptsX = [i.X for i in lstPoint]
        maxX = max(ptsX)
        for i in lstPoint:
            if i.X == maxX:
                re.append(XYZ(-1*dis/308.4 + i.X,i.Y,i.Z))
            else:
                re.append(XYZ(1*dis/308.4+i.X,i.Y,i.Z))
    else:
        ptsCompare = face.Origin.X
        for i in lstPoint:
            if i.X > ptsCompare: re.append(XYZ(-1*dis/308.4 + i.X,i.Y,i.Z))
            else: re.append(XYZ(1*dis/308.4 +i.X, i.Y,i.Z))
    return re

def PointOffset2(lstPoint, face, dis,view):
    x = view.RightDirection.X
    y = view.RightDirection.Y
    re = []
    if len(lstPoint) > 1:
        ptsX =[i.X for i in lstPoint]
        mX = max(ptsX)
        for i in lstPoint:
            if x < 0 and y == -1: # Horizaontal
                if i.X == mX:
                    re.append(XYZ(i.X, -1*dis/304.8 + i.Y, i.Z))
                else: # Vertical 
                    re.append(XYZ(i.X, 1*dis/304.8 + i.Y, i.Z))
            else:
                if i.X == mX:
                    re.append(XYZ(-1*dis/304.8 + i.X, i.Y, i.Z)) # left
                else:
                    re.append(XYZ(dis/304.8 + i.X, i.Y, i.Z)) # right
    else:
        ptsCompare = face.Origin.X # Only one floor
        for i in lstPoint:
            if i.X > ptsCompare:
                re.append(XYZ(-1*dis/304.8 + i.X, i.Y, i.Z))
            else:
                re.append(XYZ(dis/304.8 + i.X, i.Y, i.Z))
    return re



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
####--------------------------------------STEP 1-----------------------------####

getGeoFraming = [GetGeoElement(i) for i in eleFraming]
getGeoFloors = [GetGeoElement(i) for i in eleFloors]
getGeoAllEle = [GetGeoElement(i) for i in AllEle]
OUT = getGeoFraming, getGeoFloors , getGeoAllEle

getSolidFraming = [GetSolidFromGeo(i) for i in getGeoFraming]
getSolidFloors = [GetSolidFromGeo(i) for i in getGeoFloors]
getSolidAllEle = [GetSolidFromGeo(i) for i in getGeoAllEle]
OUT = getSolidFraming, getSolidFloors , getSolidAllEle

getFaceFraming = [GetPlanarFormSolid(i) for i in getSolidFraming]
getFaceFloors = [GetPlanarFormSolid(i) for i in getSolidFloors]
getFaceAllEle = [GetPlanarFormSolid(i) for i in getSolidAllEle]
OUT = getFaceFraming, getFaceFloors, getFaceFloors
OUT = [t.ToProtoType() for i in getFaceFraming for t in i ]

####--------------------------------------STEP 2-----------------------------####

getFaHoriFraming = [FilterHorizontalPlanar(i) for i in getFaceFraming]
getFaHoriFloor = [FilterHorizontalPlanar(i) for i in getFaceFloors]
getFaHoriAllEle = [FilterHorizontalPlanar(i) for i in getFaceAllEle]
OUT = getFaHoriFraming , getFaHoriFloor, getFaHoriAllEle
OUT = [t.ToProtoType() for i in getFaHoriAllEle for t in i ]

###--------------------------------------dict.fromkeys(list) or Set()-----------------------------####

re = []
reduceZ = set()
for i in getFaHoriAllEle:
    for j in i:
        if j.Origin.Z not in reduceZ:
            reduceZ.add(j.Origin.Z)
            re.append(j)
OUT = re
getFaHoriAllEle = re
####---------------------------------------------------------------------------------------####




getFaVerFraming = [FilterVerticalPlanar(i) for i in getFaceFraming]
getFaVerFloors = [FilterVerticalPlanar(i) for i in getFaceFloors]
getFaVerAllEle = [FilterVerticalPlanar(i) for i in getFaceAllEle]
OUT = [t.ToProtoType() for i in getFaVerAllEle for t in i ]
#OUT = getFaVerAllEle

####--------------------------------------STEP 3-----------------------------####

# Choose Right Or Left From User
rightFaceFraimg  =  [RightFace(i,view) for i in getFaVerFraming]
leftFaceFraimg = [LeftFace(i,view) for i in getFaVerFraming]
#OUT = [i.ToProtoType() for i in leftFaceFraimg]

rightFaceFloor = [RightFace(i,view) for i in getFaVerFloors]
leftFaceFloor = [LeftFace(i,view) for i in getFaVerFloors]
#OUT = [i.ToProtoType() for i in rightFaceFloor]

chooseFaceFraming  = GetRightOrLeftFace(lstFlattenL2(getFaVerFraming),IN[1],view) # GetRightOrLeftFace not get list input
#OUT = [chooseFaceFraming.ToProtoType()]

chooseFaceFraming  = [chooseFaceFraming]

####--------------------------------------STEP 4-----------------------------####

getLineFraming = [RetrieveEdgesFace(i) for i in chooseFaceFraming]
OUT = [j.ToProtoType() for i in getLineFraming for j in i]
OUT = lstFlattenL2(getLineFraming)

getVlineFraming = GetLineVertical(lstFlattenL2(getLineFraming))
OUT = [i.ToProtoType() for i in getVlineFraming]
OUT = getVlineFraming

####--------------------------------------STEP 5-----------------------------####

vLineOffsetFraming = LineOffset(getVlineFraming[0],IN[3],XYZ(IN[3]/304.8,0,0))
OUT =  vLineOffsetFraming.ToProtoType(),[j.ToProtoType() for i in getLineFraming for j in i]


####--------------------------------------STEP 6-----------------------------####

getFBotFraming = [GetTopOrBotFace(lstFlattenL2(getFaHoriFraming),IN[2])]
TopandBotFace = [i.ToProtoType() for i in getFBotFraming]
OUT = TopandBotFace

####--------------------------------------STEP 7-----------------------------####

getLineBotFraming = [RetrieveEdgesFace(i) for i in getFBotFraming]
OUT = [j.ToProtoType() for i in getLineBotFraming for j in i]

getHLineFraming = [GetLineMin(i) for i in getLineBotFraming]
OUT = [i.ToProtoType() for i in getHLineFraming]

hLineOffsetFraming = LineOffset(getHLineFraming[0],IN[3],XYZ(0,0,IN[3]/304.8))
OUT = hLineOffsetFraming.ToProtoType() , getHLineFraming[0].ToProtoType()



####--------------------------------------STEP 8-----------------------------####
# Show all offset line
OUT = hLineOffsetFraming.ToProtoType() , getHLineFraming[0].ToProtoType(), vLineOffsetFraming.ToProtoType(),[j.ToProtoType() for i in getLineFraming for j in i]


# ####--------------------------------------STEP 9-----------------------------####
#getRefArray - H
getRefHoriAllele = GetReferenceArray(getFaHoriAllEle)
OUT = getRefHoriAllele


# ####--------------------------------------STEP 10-----------------------------####
# #GetRefArray - V
# getVFace = [GetMaxface(i) for i in getFaVerFraming]
# getRefVertiFraming = GetReferenceArray(getVFace)

TransactionManager.Instance.EnsureInTransaction(doc)
dimV = doc.Create.NewDimension(view, vLineOffsetFraming, getRefHoriAllele)
TransactionManager.Instance.TransactionTaskDone()

# OUT = dimV
faceTopFraming = GetRightOrLeftFace(lstFlattenL2(getFaVerFraming),True,view)


ptsUse = []

if len(eleFloors)> 0:
    ptsFlatten = []
    ptsIntersect = []
    ptsRemove = []
    ###----------------------------------------CropView-----------------------------####
    cropview = view.GetCropRegionShapeManager().GetCropShape()
    ####---------------------------------------GetLineVertical----------------------####
    lineCrop = lstFlattenL2([GetLineVertical(i) for i in cropview])
    OUT = lineCrop,[i.ToProtoType() for i in lineCrop]
    ###----------------------------------------Geometry-----------------------------####
    geoFloors = [GetGeoElement(i) for i in eleFloors]
    solid = GetSolidFromGeo(lstFlattenL2(geoFloors))
    plannarFloors = GetPlanarFormSolid(solid)
    faceTopFloor = GetTopFacesEle(plannarFloors)
    for i in faceTopFloor:
        for j in lineCrop:
            ptsIntersect.append(GetIntersection(i,j))
    ptsFlatten =lstFlattenL2(ptsIntersect)
    ptsRemove = list(filter(None,ptsFlatten))
    ptsUse = PointOffset2(ptsRemove,80,faceTopFraming, view)

OUT = ptsRemove

familyBreak = []

TransactionManager.Instance.EnsureInTransaction(doc)
for i in ptsUse:
    faceBreak  = doc.Create.NewFamilyInstance(i,UnwrapElement(IN[4]),view)
    familyBreak.append(faceBreak)
TransactionManager.Instance.TransactionTaskDone()
