import clr
import System
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

# clr.AddReference('RevitAPI')
# import Autodesk
# from Autodesk.Revit.DB import *

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





###################################List - Modifily #####################
def filtered(lstScores, number): # Filter number of list with a condition
    fil = filter(lambda score: score < number, lstScores)
    return (list(fil))
def filter_IsListInList(lst1,lst2):
    re = []
    for i in len(lst1):
        re.append(i)
def chunks(l, n): #List.Chop
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))
def GetIndexOfList(lst,index): # Get a Value from Level 3 of a list by Index Number
    re = []
    for i in lst:
        c = i[index]
        re.append(c)
    return re
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
################################### GEOMETRY ELEMENTS #####################
def CreateLine(point1,point2): # Take Revit.DB.Line by XYZ.Bisis
    line = Line.CreateBound(point1,point2)
    return line
def ReferenceFromSurface(ElementSurface): # Get Revit.DB.Reference from Surface
    ref = []
    for i in ElementSurface:
        re =[]
        for j in i:
            re.append(j.Tags.LookupTag("RevitFaceReference"))
        ref.append(re)
    return ref
    #OUT = ReferenceFromSurface(UnwrapElement(IN[1]))
def GetDBLineFormEleLine(ElementLines): # Get Revit.DB.Line from Curve Elements
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    ln = []
    for i in lines:
        re =[]
        for j in i:
            re.append(UnwrapElement(j).ToRevitType())
        ln.append(re)
    return ln
    #OUT = GetDBLineFormEleLine(IN[1])
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
    #OUT = GetReferenceOfGrid(IN[1])
def Combine_EleSurface_EleCurve_RefGrids(EleCurve,EleSurface,RefGrids): # Combine Ref's Surface and Ref
    Ref=[]
    for i in range(0,len(EleSurface)):
        dis =[]
        for j in EleSurface[i]:
            dis.append(EleCurve[i].DistanceTo(j))
        if dis[0] !=0 and dis[1] !=0:
            #su[i].insert(0,lst[i])
            out = EleSurface[i].insert(0,RefGrids[i])
            
    for i in range(0,len(EleSurface)):
        re =[]
        for j in EleSurface[i]:
            if str(j).Contains('Surface'):
                re.append(j.Tags.LookupTag("RevitFaceReference"))
            else:
                re.append(j)
        Ref.append(re)
    return Ref
    #OUT = Combine_EleSurface_EleCurve_RefGrids(IN[1],IN[2],IN[3])

def GetGeoElement(element): # Get geometry of element.
    geo = []
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.DetailLevel = ViewDetailLevel.Fine
    geoByElement = element.get_Geometry(opt)
    geo = [i for i in geoByElement]
    return geo
    #getGeoFraming = [GetGeoElement(i) for i in eleFraming]
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
    #getSolidFraming = [GetSolidFromGeo(i) for i in getGeoFraming]
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
def FilterVerticalPlanar(lstPlface): # Get Vertical PlannarFaces 
    faV = []
    y = XYZ.BasisY
    for i in lstPlface:
        faNomal = i.FaceNormal
        check  = Isparalel(y,faNomal)
        if check == True:
            faV.append(i)
    return faV
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

def GetMaxface(plananrs):
    _Area = []
    _face = []
    for i in plananrs:
        _Area.append(i.Area)
    for j in plananrs:
        if j.Area > (max(_Area)-min(_Area)):
            _face.append(j)
            
    return _face
    #getFaMaxVerFraming = [GetMaxface(i) for i in getFaVerFraming]

def FilterHorizontalPlanar(lstPlface): # Get Horizaontal PlannarFaces 
    faH = []
    z = XYZ.BasisZ
    for i in lstPlface:
        check = Isparalel(z, i.FaceNormal)
        if check == True:
            faH.append(i)
    return faH
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
    #GetLineFraming = [RetrieveEdgesFace(i) for i in getFaVerFraming[0]]

def GetLineMin(lstLine): # Get a min line of list line
    _length = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == min(_length):
            return j  
def GetLineMax(lstLine): # Get a max line of list line
    _length = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == max(_length):
            return j   
 
def LineOffset(line,distance,direc): # Offset a line from one line earlier
    convert = distance/304.8
    newVector = None
    # if direc == "x" or "X": newVector = XYZ(convert,0,0)
    # if direc == "y" or "Y": newVector = XYZ(0,convert,0)
    # elif direc == "z" or "Z": newVector = XYZ(0,0,convert)
    newVector = XYZ(0,0,convert)
    newVector = XYZ(0,convert,0)
    trans = Transform.CreateTranslation(newVector) # Setting direction for GetLinMin
    lineMove = line.CreateTransformed(trans)
    return lineMove 
def GetReference(lstPlanar):
    re = []
    for i in lstPlanar:
        re.append(i.Reference)
    return re
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
        if Isparalel(NorLo, NorRevit):
            re.append(i)
    return re

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
def LinebyGrids(lstGrids):
    re = []
    for i in lstGrids:
        crv = i.Curve
        re.append(crv)
    return re
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
        #offsetline =LineOffset(line,IN[1],"X",direcFraming, IN[2] )


def RefArrayByEleLine(linelist): # Get ReferenceArray by Element Line
    refArray = []
    for i in linelist:
        rArr = ReferenceArray()
        for l in i:
            rArr.Append(Reference(l))
        refArray.append(rArr)
    return refArray
    #OUT = RefArrayByEleLine(UnwrapElement(IN[2]))

###-------------------------GEOMETRY---------------------###
def getAngle(p1,p2):
    xDiff = p2.X - p1.X
    yDiff = p2.Y - p1.Y
    radian = math.atan2(yDiff, xDiff) # Define Angle in Euclide Surface 
    angle = math.degrees(radian) 
    angle = abs(angle) 
    angle = round(angle)
    return angle
    # p1 = XYZ(0,0,1)
    # p2 = XYZ(0,1,0)
    # OUT = getAngle(p1,p2)

def distance(s,e):#Hypot is a mathematical function defined to calculate the length of the hypotenuse of a right-angle triangle
    dist = math.hypot(e.X - s.X,e.Y-s.Y)
    return dist
    # p1 = Point.ByCoordinates(1,0)
    # p2 = Point.ByCoordinates(10,10)
    # OUT = distance(p1,p2)
def distance(p1,p2):
    """Caculates the distance between two points in 2D (XY) space"""
    x = p2.X - p1.X
    y = p2.Y - p1.Y
    return math.sqrt(x**2 +y**2)
    # p1 = Point.ByCoordinates(1,0)
    # p2 = Point.ByCoordinates(10,10)
    # OUT = distance(p1,p2)

def LineByTwoPoint(p1,p2):
    line = Line.ByStartPointEndPoint(p1,p2)
    return line
p1 = Point.ByCoordinates(1,0,10)
p2 = Point.ByCoordinates(10,10,0)
p3 = Point.ByCoordinates(10,5,7)

# l1 = LineByTwoPoint(p1,p2)
# l2 = LineByTwoPoint(p1,p3)
# OUT = l1,l2

# def AngleTwoLine(line1,line2):
#     angle = line1.AngleTo(line2)
#     return angle

# OUT = AngleTwoLine(l1,l2)