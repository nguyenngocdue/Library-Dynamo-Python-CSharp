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
def getPlanarFormSolid(solids): # Get Planarface from solids
    plaf = []
    for i in solids:
        var = i.Faces
        for j in var:
            if j.Reference != None:
                plaf.append(j)
    return plaf
def removeFaceNone(dbPlanarFaces): # Get planarFaces Not Null Value
    pfaces = []
    for i in dbPlanarFaces:
        if i.Reference != None:
            pfaces.append(i)
    return pfaces
def isParalel(p,q):
    return p.CrossProduct(q).IsZeroLength()
def FilterVerticalPlanar(lstPlface): # Get Vertical PlanarFaces 
    faV = []
    x = XYZ.BasisX # You can change that value to have a new direction
    for i in lstPlface:
        faNomal = i.FaceNormal
        check  = Isparalel(x,faNomal)
        if check == True:
            faV.append(i)
    return faV
def FilterHorizontalPlanar(lstPlface): # Get Horizaontal PlanarFaces 
    faH = []
    z = XYZ.BasisZ
    for i in lstPlface:
        check = Isparalel(z, i.FaceNormal)
        if check == True:
            faH.append(i)
    return faHdef isParalel(p,q):
    return p.CrossProduct(q).IsZeroLength()
     
def getLeftRightPlannarFaces(plannars): # Get Vertical PlanarFaces 
    re = []
    plannars = removeFaceNone(plannars)
    for i in plannars:
        normalVector = i.FaceNormal
        x =  XYZ.BasisX
        y =  XYZ.BasisY
        rad = normalVector.AngleTo(XYZ.BasisZ)
        isPararelX = isParalel(normalVector, x)
        isPararelY = isParalel(normalVector, y)
        if not isPararelX and isPararelY and 30<(rad*180/3.14)<170:
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
def getRightOrLeftPlanarFaces(dbPlanarFaces,reason,activeView): # Choose in one of Right and Left of Faces
    if reason == True: return getRightDbPlanarFaces(dbPlanarFaces,activeView)
    elif reason == False: return getLeftDbPlanarFaces(dbPlanarFaces, activeView)
def getTopOrBotFace(lstPlanars, reason): # Get Top or Bottom of Faces
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
def getLineMin(lstLine): # Get a min line of list line
    _length = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == min(_length):
            return j   
def LineOffset(line,distance,direct): # Offset a line from one line earlier
    convert = distance/304.8
    if direct == "x" or "X": newVector = XYZ(convert,0,0)
    if direct == "y" or "Y": newVector = XYZ(0,convert,0)
    if direct == "z" or "Z": newVector = XYZ(0,0,convert)
    # newVector = XYZ(convert,0,0)
    # newVector = XYZ(0,0,convert)

    trans = Transform.CreateTranslation(direct) # Setting direction for GetLinMin
    lineMove = line.CreateTransformed(trans)
    return lineMove 
def getReferenceArray(planars):
    reArray = ReferenceArray()
    for i in planars:
        reArray.Append(i.Reference)
    return reArray
def getLineVertical(lstLine): # Get vertical Line by Isparalel
    re = []
    NorRevit = XYZ.BasisZ
    for i in lstLine:
        NorLo = i.Direction
        if Isparalel(NorLo, NorRevit):
            re.append(i)
    return re
def getMaxface(plananrs):
    _Area = []
    _face = []
    for i in plananrs:
        _Area.append(i.Area)
    for j in plananrs:
        if j.Area > (max(_Area)-min(_Area)):
            _face.append(j)
            
    return _face

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
rightFaceFraimg  =  [getRightDbPlanarFaces(i,view) for i in getFaVerFraming]
leftFaceFraimg = [getLeftDbPlanarFaces(i,view) for i in getFaVerFraming]
#OUT = [i.ToProtoType() for i in leftFaceFraimg]

rightFaceFloor = [getRightDbPlanarFaces(i,view) for i in getFaVerFloors]
leftFaceFloor = [getLeftDbPlanarFaces(i,view) for i in getFaVerFloors]
#OUT = [i.ToProtoType() for i in rightFaceFloor]

chooseFaceFraming  = GetRightOrLeftFace(lstFlattenL2(getFaVerFraming),IN[1],view) # GetRightOrLeftFace not get list input
#OUT = [chooseFaceFraming.ToProtoType()]

chooseFaceFraming  = [chooseFaceFraming]

####--------------------------------------STEP 4-----------------------------####

getLineFraming = [RetrieveEdgesFace(i) for i in chooseFaceFraming]
#OUT = [j.ToProtoType() for i in getLineFraming for j in i]
#OUT = lstFlattenL2(getLineFraming)

getVlineFraming = GetLineVertical(lstFlattenL2(getLineFraming))
#OUT = [i.ToProtoType() for i in getVlineFraming]
#OUT = getVlineFraming

####--------------------------------------STEP 5-----------------------------####

vLineOffsetFraming = LineOffset(getVlineFraming[0],IN[3],XYZ(IN[3]/304.8,0,0))
#OUT =  vLineOffsetFraming.ToProtoType(),[j.ToProtoType() for i in getLineFraming for j in i]


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



