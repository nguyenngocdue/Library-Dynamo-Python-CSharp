"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
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

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument


#-------------------------------------------------------------List - Modifily-----------------------------------------------#
def ClearList(primList):
    result = []
    for sublist in primList:
        if sublist is "":
            continue
        elif sublist is None:
            continue 
        if isinstance(sublist, list):
             sublist = ClearList(sublist)
             if not sublist:
                 continue
        result.append(sublist)
    return result

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
    #OUT = chunks(IN[1])
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
def RemoveValueNone(lst): # Get Value Not Null Value
    value = []
    for i in lst:
		if i == None: value.append(i)
		else: value.append(i)
		return value
    OUT = [RemoveValueNone(i) for i in IN[1]]

def GetFace_Zmax(lstPlface): # Get Horizaontal PlannarFaces 
    coor_Z = []
    faH = []
    index = []
    for i in lstPlface:
    	coor_Z.append(i.Origin.Z)
    for idx, j in enumerate(lstPlface):
        r1 = []
        get_inx = []
        if j.Origin.Z >= max( coor_Z):
            r1.append(j)
            get_inx.append(idx)
        faH.append(r1)
        index.append(get_inx)
    return faH
def getOrigin_level (lstPlanar):
    re = []
    for i in ele:
        r1 = []
        for j in i:
            ori =j.Origin
            r1.append(ori)
        re.append(r1)
    return re
    # ele = IN[1]
    # OUT = getOrigin_level (ele)
#--------------------------------------------------------------GEOMETRY ELEMENTS-----------------------------------------------------------####
def CreateLine(xyzp1,xyzp2): # Take Revit.DB.Line by XYZ.Bisis
    lineDB = Line.CreateBound(xyzp1,xyzp2)
    return lineDB
def CreateLine(point1,point2): # Take Revit.DB.Line by XYZ.Bisis
    lineDB = Line.CreateBound(point1.ToXyz(),point2.ToXyz())
    return lineDB

def CreateLine(xyzp1,xyzp2): # Take Revit.DB.Line by XYZ.Bisis
    lineDB = Line.CreateBound(xyzp1,xyzp2)
    return lineDB


# ele = IN[1]

# re = []
# for i in ele:
#     dbLine = CreateLine(i[0], i[1])
#     re.append(dbLine)
    
# OUT = re
def ReferenceFromSurface(ElementSurface): # Get Revit.DB.Reference from Surface
    ref = []
    for i in ElementSurface:
        re =[]
        for j in i:
            re.append(j.Tags.LookupTag("RevitFaceReference"))
        ref.append(re)
    return ref
    #OUT = ReferenceFromSurface(UnwrapElement(IN[1]))
def getDBLineFormEleLine(ElementLines): # Get Revit.DB.Line from Curve Elements
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    ln = []
    for i in ElementLines:
        re =[]
        for j in i:
            re.append(UnwrapElement(j).ToRevitType())
        ln.append(re)
    return ln
    #OUT = GetDBLineFormEleLine(IN[1])
def getDBLineFormEleLine(ElementLines): # Get Revit.DB.Line from Curve Elements
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    ln = []
    for i in ElementLines:
        ln.append(UnwrapElement(i).ToRevitType())
    return ln

def GetRefOfGrid(ElementGrids): # Get Revit.DB.Reference from Grids
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    refGrids = []

    for i in UnwrapElement(ElementGrids):
        f = (i.get_Geometry(opt))
        [refGrids.append(j.Reference) for j in f if str(j).Contains("Line")]
    return refGrids
    #OUT = GetRefOfGrid(IN[1])
def GetRefArrayByEleLine(linelist): # Get ReferenceArray by Element Line
    refArray = []
    for i in linelist:
        rArr = ReferenceArray()
        for l in i:
            rArr.Append(Reference(l))
        refArray.append(rArr)
    return refArray
    #OUT = GetRefArrayByEleLine(UnwrapElement(IN[2]))
def GetRef(lstPlanar):
    re = []
    for i in lstPlanar:
        re.append(i.Reference)
    return re
def GetRefArray(lstPlanar):
    reArray = ReferenceArray()
    for i in lstPlanar:
        reArray.Append(i.Reference)
    return reArray
    #OUT = GetReferenceArray(IN[1])
def GetRefArrayFromRef(ref):
    re = ReferenceArray()
    for i in ref:
        re.Append(i)
    return re
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
    
def GetLocationPoint(element): # Get LocationPoint of element.
    re = []
    re.append(element.Location.Point)
    return re
    #OUT = [GetLocationPoint(i) for i in UnwrapElement(IN[1])]

def GetPointFromGeo(lstGeo):
    pts = []
    for i in lstGeo:
        if i.GetType() == Point:
            pts.append(i)
    return pts
    #OUT = [GetPointFromGeo(i) for i in IN[1]]

def mappingXYZ_to_xoz_plane(lstXYZ):
    reesult = []
    for _xyz in lstXYZ:
        x = _xyz.X
        y = _xyz.Y
        z = 0
        xyz = XYZ(x, y, z)
        reesult.append(xyz)
    return reesult

lstXYZ = mappingXYZ_to_xoz_plane(IN[1])
OUT = lstXYZ

data = IN[0]
def removeDuplicatesXYZ(data):
    unique_points = set()
    for xyz in data:
        x, y, z = round(xyz.X, 6), round(xyz.Y, 6), round(xyz.Z, 6)
        unique_points.add((x, y, z))
    result = [XYZ(x, y, z) for x, y, z in unique_points]
    return result
OUT = removeDuplicatesXYZ(data)
    

def removeDuplicateXYZ(lstXYZ):
    distinct_points = list(set(lstXYZ))
    return distinct_points
OUT = removeDuplicateXYZ( IN[1])

def getXYZByDBLines(dbLines):
	points = []
	for dbLine in dbLines:
		start_point = dbLine.GetEndPoint(0)
		end_point = dbLine.GetEndPoint(1)
		points.append(start_point)
		points.append(end_point)
	return points

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

def GetGeoElement(element): # Get geometry of element.
    geo = []
    opt = Options()
    geoByElement = element.get_Geometry(opt)
    geoEnum = geoByElement.GetEnumerator(); geoEnum.MoveNext()
    geoNext = geoEnum.Current.GetInstanceGeometry()
    geo = [i for i in geoNext]
    out = []
    for i in geo:
    	if i.GetType()== Solid and i.Volume > 0:	
    		out.append(i)	
		if i.GetType() == GeometryInstance:	
			var = i.SymbolGeometry
			for j in var:
				if j.Volume > 0:
					out.append(i)
    return out
    getGeoFraming = [GetGeoElement(i) for i in element]

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
def GetSolidFromGeo(lstGeo): # Get Solid from Geo
    sol = []
    for i in lstGeo:
        if type(i)== Autodesk.Revit.DB.Solid and i.Volume > 0:
            sol.append(i)
        elif type(i)== Autodesk.Revit.DB.GeometryInstance:
            var = i.SymbolGeometry
            for j in var:
                if type(j)== Autodesk.Revit.DB.Solid and j.Volume > 0:
                    sol.append(j)
        	sol.append(j)
    return sol
    #getSolidFraming = [GetSolidFromGeo(i) for i in IN[1]]
def GetPlanarFormSolid(solids): # Get Planarface from solids
    plaf = []
    for i in solids:
        var = i.Faces
        for j in var:
            if j.Reference != None:
                plaf.append(j)
    return plaf
    #getFaceFraming = [GetPlanarFormSolid(i) for i in getSolidFraming]
def calculateFacesArea(faces):
    total_area = 0.0
    for face in faces:
        total_area += face.Area
    return total_area
areas = calculateFacesArea(IN[0])
OUT = areas
def RemoveFaceNone(lstplanars): # Get planarFaces Not Null Value
    pfaces = []
    for i in lstplanars:
        if i.Reference != None:
            pfaces.append(i)
    return pfaces
def Isparalel(p,q):
    return p.CrossProduct(q).IsZeroLength()
def FilterHorizontalPlanar(lstPlface): # Get Horizaontal PlannarFaces 
    faH = []
    z = XYZ.BasisZ # You can change that value to have a new direction
    for i in lstPlface:
    	if type(i) == Autodesk.Revit.DB.PlanarFace:
            check = Isparalel(z, i.FaceNormal)
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
def GetMaxface(plananrs):
    _Area = []
    _face = []
    for i in plananrs:
        _Area.append(i.Area)
    for j in plananrs:
        if j.Area > max(_Area)-0.5:
            _face.append(j)


def sortPlanarFace(lstPlanar):
    if (round(ele[0][0].FaceNormal.X) != 0): 
        return sorted(ele, key = lambda ele : [i.Origin.X for i in ele], reverse= False)
    else:
        return sorted(ele, key = lambda ele : [i.Origin.Y for i in ele], reverse= False)
    # test = [i.FaceNormal for j in ele for i in j]
    # OUT = [round(i.X) == 0 if True else False for i in test]
    # ele = IN[1]
    # OUT = sortPlanarFace(ele)

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
           # OUT = [GetLineMin(i) for i in IN[1]]  
def GetLineMax(lstLine): # Get a max line of list line
    _length = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == max(_length):
            return j   
    OUT = [GetLineMax(i) for i in IN[1]]  
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
def LineOffset(line, distance, direc): #Offset Revit.DB.Line
    convert = distance/304.8
    newVector = None
    if direc == "X": newVector = XYZ(convert,0,0)
    if direc == "Y": newVector = XYZ(0,convert,0)
    if direc == "Z": newVector = XYZ(0,0,convert)

    trans = Transform.CreateTranslation(newVector)
    lineMove = line.CreateTransformed(trans)
    return lineMove

    #dimLine = [LineOffset(i,IN[4],"Z") for i in linePlace][0]
def GetLineVertical(lstLine): # Get vertical Line by Isparalel
    re = []
    NorRevit = XYZ.BasisZ
    for i in lstLine:
        NorLo = i.Direction
        if Isparalel(NorLo, NorRevit):
            re.append(i)
    return re
    #getVlineFraming = [GetLineVertical(i) for i in lines]
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

        # ele = SelectionFilter("Grids", "Structural Framing")
        # elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")
        # elSelect= [elSelectAll[0]]
        # eleFraming = elSelectAll[1]

            # ele = SelectionFilter("Grids", "Lines")
            # elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")
            # OUT = elSelectAll

            # lines = []
            # grids = []
            # for i in elSelectAll:
            #     if i.Category.Name == "Lines": lines.append(i)
            #     if i.Category.Name == "Grids": grids.append(i)
            # OUT =  lines, grids
class SelectionFilter(ISelectionFilter):
	def __init__(self, ctgName):
		self.ctgName = ctgName
	def AllowElement(self, element):
		if element.Category.Name == self.ctgName:
			return True
		else:
			return False
	def AllowReference(ref, xyZ):
		return False

    # selFilter = SelectionFilter("Grids")
    # elSelect = uidoc.Selection.PickElementsByRectangle(selFilter,"Selects")
def DBLinebyGrids(lstGrids):
    re = []
    for i in lstGrids:
        re.append(i.Curve)
    return re
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
def GetToProtoType(items):
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    re = []
    for i in items:
        r1 = []
        for j in i:
            r1.append(j.ToProtoType())
        re.append(r1)
    return re
    OUT = GetToProtoType(IN[1])
def GetIntersection(face, line):
    re = []
    results = clr.Reference[IntersectionResultArray]()
    intersect = face.Intersect(line, results)
    if intersect == SetComparisonResult.Overlap:
        var1 = results.Item[0]
        var2 = var1.XYZPoint
        re.append(var2)
    return re

    #OUT = [GetIntersection(i,j) for i,j in zip(IN[1], IN[2])]
###--------------------------------------------------GEOMETRY---------------------------------------------------------###
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
def lineByTwoPoint(p1,p2):
    line = Line.ByStartPointEndPoint(p1,p2)
    return line
    #OUT = lineByTwoPoint(IN[1][0],IN[1][1])
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
def CretePointXYZ(numberX,numberY,numberZ):
    TransactionManager.Instance.EnsureInTransaction(doc)
    pts = []
    for i in zip(numberX,numberY,numberZ):
        pts.append(Point.ByCoordinates(i,i,i))
    TransactionManager.Instance.TransactionTaskDone()
def LineByTwoPoint(p1,p2):
    line = Line.ByStartPointEndPoint(p1,p2)
    return line
def AngleTwoLine(line1,line2):
    angle = line1.AngleTo(line2)
    return angle
    #OUT = AngleTwoLine(l1,l2)
def MidPointOfPoint(x,y):
	return 0.5*(x+y)
def MidPoint (line):
	return MidPointOfPoint(line.GetEndPoint(0),line.GetEndpoint(1))
###------------------------------------------------ Pick Object ---------------------------------------------------------###
def pickObject():
    from Autodesk.Revit.UI.Selection import ObjectType
    picked = uidoc.Selection.PickObjects(ObjectType.Element)
    return picked
def pickObject():
    from Autodesk.Revit.UI.Selection import ObjectType
    refs = uidoc.Selection.PickObject(ObjectType.Element)
    return  doc.GetElement(refs.ElementId)	

def pickObjects():
    from Autodesk.Revit.UI.Selection import ObjectType
    refs = uidoc.Selection.PickObjects(ObjectType.Element)
    return  [doc.GetElement(i.ElementId) for i in refs]	

def pickObjectsFilter(filter):
	el_ref = uidoc.Selection.PickObjects(ObjectType.Element, filter)
	typelist = list()
	for i in el_ref:
		try:
			typelist.append(doc.GetElement(i.ElementId))
		except:
			typelist.apped(list())
	return typelist			
    # ele = SelectionFilter("Structural Framing", "Levels")
    # OUT = pickObjectFilter(ele)
###------------------------------------------------ Element ---------------------------------------------------------###
def GetBicFromInput(var):	
	bic = None
	if var:
        cattype = var.GetType().ToString()
        if cattype == "Revit.Elements.Category":
            bic = System.Enum.ToObject(BuiltInCategory, var.Id)
		elif cattype == "Autodesk.Revit.DB.BuiltInCategory": bic = var
		elif cattype == "System.String": 
			found = [x for x in bics if x.ToString() == var]
			if len(found) > 0:
                bic = found[0]
	return bic
def ElementsByCategory(bic, doc):
	collector = FilteredElementCollector(doc).OfCategory(bic).WhereElementIsNotElementType()
	return collector.ToElements()
###------------------------------------------------ VIEW ---------------------------------------------------------###
def GetView( view,doc):
	numview = view.ViewTemplateId
	if numview.IntegerValue  == -1:
		return doc.ActiveView
	else: 
		return  doc.GetElement(numview)
###------------------------------------------------ Get All Family ---------------------------------------------------------###

def Get_Dicof_FamilyNames(category):
	collector = FilteredElementCollector(doc).OfCategory(category).WhereElementIsElementType().ToElements()
	All_Families = {}
	for family in collector:
		name = family.FamilyName
		if name not in All_Families.keys():
			All_Families[name]= family
	return (All_Families)
# Get OST of BuilinCategory
def getBuilIncategory_OTS(nameCategory): # Get Name of BuiltInCategory
    return [i for i in System.Enum.GetValues(BuiltInCategory) if str(i) == "OST_"+nameCategory]
def getAllFamilyOfBuiltInCategory(OST_cateNane): # Get all family from BuilInCategory
    collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PlumbingFixtures).OfClass(FamilySymbol).ToElements()
    families = set()
    for type in types:
	    families.add(type.Family)
    families = list(families)
    return families
def getAllFamilyOrFamilyType_RVT(ofClass): # get All Family Or FamilyType Of RVT
    """OfClass:
    Autodesk.Revit.DB.Familt :  If you get All Family in RVT
    ElementType : If you get FamilyType
    See Example "get_ElementType = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.Family).ToElements()"
    Dynamo Node to See Type of "OfCalss" : Element Types
    """
    getAllFaRVT = FilteredElementCollector(doc).OfClass(ofClass).ToElements()
    return getAllFaRVT
###------------------------------------------------ List ---------------------------------------------------------###
def irange(start,end,step):
    #     import clr
    # start = IN[0]
    # end = IN[1]
    # step = IN[2]
	
	res = [start]
	if step == 1:
		return res
	if step == 2:
		res.append(end)
		return res
	if step > 2:
		a = (end-start)/(step-1)
		t = step - 2
		ans = start
		for i in range(t):
			ans+=a
			res.append(ans)
		res.append(end)
		return res
    # a=irange(start,end,step)
    # OUT = a	

###------------------------------------------------ Surface ---------------------------------------------------------###

# Translate From Point To Surface:
    ptslist = chop(ptslist, len1)  # phân chia cấp list từ ptslist
    f_sf1 = Surface.ByPerimeterPoints
    sflist = [f_sf1(pts) for i in ptslist for pts in i ]


###------------------------------------------------ BoundingBox ---------------------------------------------------------###
    import clr
    clr.AddReference("RevitAPI")
    from Autodesk.Revit.DB import *
    #The inputs to this node will be stored as a list in the IN variables.
    elements = UnwrapElement(IN[0])
    points =[]
    for e in elements:
      bb = e.get_BoundingBox(None)
      if not bb is None:
        centre = bb.Min+(bb.Max-bb.Min)/2
        points.append(centre)
    #Assign your output to the OUT variable.
    OUT = points

ele = [familyInstance]
elemType = [doc.GetElement(i.GetTypeId()) for i in ele]
TransactionManager.Instance.EnsureInTransaction(doc)
getBoundringMax = [i.get_BoundingBox(None).Max for i in elemType]
getBoundringMin = [i.get_BoundingBox(None).Min for i in elemType]
TransactionManager.Instance.TransactionTaskDone()

# Code 
#Preparing input from dynamo to revit
element = UnwrapElement(IN[0])
re = []
for i in element:
	re.append(i.get_BoundingBox(doc.ActiveView))
OUT = re

# Outline
eleA = IN[1]
solB = IN[2]
re = []
for i in eleA:
    re.append(Outline(i.Min, i.Max))
OUT = re

###------------------------------------------------ ReadFile ---------------------------------------------------------###

f = open("demofile.txt", "r")
print(f.read())

###------------------------------------------------ MEP ---------------------------------------------------------###

def getCurveOfPipes(lstEle):
    toList = lambda x : x if hasattr(x, '__iter__') else [x]
    lstElemNetWork = toList(UnwrapElement(lstEle))
    lstDS_Geo = [] 
    for e in lstElemNetWork:
        if isinstance(e.Location, LocationCurve):
            rvtCurve = e.Location.Curve
            lstDS_Geo.append(rvtCurve)
        else:
            locPt = e.Location.Point
            connSet = e.MEPModel.ConnectorManager.Connectors
            lstConn = list(connSet)
            if connSet.Size == 2: # connectors of family
                try:
                    pline = PolyLine.Create(List[XYZ]([lstConn[0].Origin, locPt, lstConn[1].Origin]))
                    lstDS_Geo.append(pline)
                except:  
                    # Unable to create Line. Points are likely coincident
                    line = Line.CreateBound(lstConn[0].Origin, lstConn[1].Origin)
                    lstDS_Geo.append(line)			
            else:
                for con in connSet:
                    line = Line.CreateBound(locPt, con.Origin)
                    lstDS_Geo.append(line)

            return lstDS_Geo
    #OUT = getCurveOfPipes(IN[1])

def getRefFromElement(lstElement):
    ref=[]
    for element in lstElement:
        if isinstance (element, Autodesk.Revit.DB.Dimension):
            ref.append(element.References)
        elif isinstance (element, Autodesk.Revit.DB.ReferencePlane):
            ref.append(element.GetReference())
        else : ref.append(Reference(element))
    return ref

def getBoundringMax(lstSolids):
    maxXYZ = []
    for i in lstSolids:
        maxXYZ.append(i.GetBoundingBox().Max)
    return maxXYZ

def getBoundringMin(lstSolids):
    minXYZ = []
    for i in lstSolids:
        minXYZ.append(i.GetBoundingBox().Min)
    return minXYZ
    #OUT = [getBoundringMax(i) for i in IN[1]],

def getCentroidPoint(lstSolids): #middle point 
    xyzCentroiPoint = []
    for i in lstSolids:
        xyzCentroiPoint.append(i.ComputeCentroid())
    return xyzCentroiPoint

def getGeoElement(element, doc , view): # Get geometry of element.
    geo = []
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    #opt.DetailLevel = ViewDetailLevel.Coarse

    opt.View = UnwrapElement(view)
    geoByElement = element.get_Geometry(opt)
    geo = [i for i in geoByElement]
    return geo

def getRefFromDBLine(lstDBLine): # Get reference
    ref = ReferenceArray()
    for i in lstDBLine:
        ref.Append(i.GetEndPointReference(1))
    return ref

def filterDBLine(lstGeo): # Get DBLine from Geo
    dbLine = []
    for i in lstGeo:
        if i.GetType() == Autodesk.Revit.DB.Line:
            dbLine.append(i)
    return dbLine[0]

def filterDBSolid(lstGeo): # Get DBSokid from Geo
    dbSolid = []
    for i in lstGeo:
        if i.GetType() == Autodesk.Revit.DB.Solid:
            dbSolid.append(i)
    return dbSolid[0]

def getVectorOfDBLine(lstDBline): # Get Vector from DBLine
    vec = []
    for i in lstDBline:
        pts1Line = i.GetEndPoint(0)
        pts2Line = i.GetEndPoint(1)
        vec.append(pts1Line - pts2Line)
    return vec

def setBasic(x):
    if x == "x":
        return XYZ.BasisX
    elif x == "y":
        return XYZ.BasisY
    else:
        return XYZ.BasisZ

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Vector, Point, Line
import Autodesk.DesignScript.Geometry as DS
def getVectorFromPoints(start_point, end_point):
    vector = Vector.ByTwoPoints(start_point, end_point)
    return vector
start_point = UnwrapElement(IN[0])
end_point = UnwrapElement(IN[1])
OUT =  getVectorFromPoints(start_point, end_point)


def getVectorOfDBLine(lstDBline):
    vec = []
    pts1Line = [i.GetEndPoint(0) for i in lstDBline]
    pts2Line = [i.GetEndPoint(1) for i in lstDBline]
    for j,i in zip(pts1Line,pts2Line):
        vec.append(j-i)
    return vec

def extendLine(lstDBLine,distance):
    def CreateLine(point1,point2): # Take Revit.DB.Line by XYZ.Bisis
        line = Line.CreateBound(point1,point2)
        return line

    #0: End point , #1: StartPoint
    startPoint = [i.GetEndPoint(1) for i in lstDBLine]
    endPoint = [i.GetEndPoint(0) for i in lstDBLine]
    
    x_startPoint = [i.GetEndPoint(1).X for i in lstDBLine]
    y_startPoint = [i.GetEndPoint(1).Y for i in lstDBLine]
    z_startPoint = [i.GetEndPoint(1).Z for i in lstDBLine]
    x_endPoint = [i.GetEndPoint(0).X for i in lstDBLine]
    y_endPoint = [i.GetEndPoint(0).Y for i in lstDBLine]
    z_endPoint = [i.GetEndPoint(0).Z for i in lstDBLine]

    if x_startPoint == x_endPoint:
        extend = -distance/304.8
        pxExStart = [i.Y - extend for i in startPoint]
        pxExEnd = [i.Y + extend for i in endPoint]

        y = pxExStart
        x = [i.X for i in startPoint]
        z = [i.Z for i in startPoint]
        p1 = [XYZ(x1,y1,z1) for x1,y1,z1 in zip(x,y,z)]

        y2 = pxExEnd
        x2 = [i.X for i in endPoint]
        z2 = [i.Z for i in endPoint]
        p2 = [XYZ(x2,y2,z2) for x2,y2,z2 in zip(x2,y2,z2)]
        return [CreateLine(i,j) for i,j in zip(p2,p1)]
        
    elif y_startPoint == y_endPoint:
        extend = -distance/304.8
        pxExStart = [i.X - extend for i in startPoint]
        pxExEnd = [i.X + extend for i in endPoint]

        y = pxExStart
        x = [i.X for i in startPoint]
        z = [i.Z for i in startPoint]
        p1 = [XYZ(x1,y1,z1) for x1,y1,z1 in zip(x,y,z)]

        y2 = pxExEnd
        x2 = [i.X for i in endPoint]
        z2 = [i.Z for i in endPoint]
        p2 = [XYZ(x2,y2,z2) for x2,y2,z2 in zip(x2,y2,z2)]
        return [CreateLine(i,j) for i,j in zip(p2,p1)]

    elif z_startPoint != z_endPoint:
        extend = -distance/304.8
        pxExStart = [i.Z - extend for i in startPoint]
        pxExEnd = [i.Z + extend for i in endPoint]

        y = pxExStart
        x = [i.X for i in startPoint]
        z = [i.Z for i in startPoint]
        p1 = [XYZ(x1,y1,z1) for x1,y1,z1 in zip(x,y,z)]

        y2 = pxExEnd
        x2 = [i.X for i in endPoint]
        z2 = [i.Z for i in endPoint]
        p2 = [XYZ(x2,y2,z2) for x2,y2,z2 in zip(x2,y2,z2)]
        return [CreateLine(i,j) for i,j in zip(p2,p1)]
    OUT = extendLine(IN[1],IN[2])

#Fix
def extendLine(lstDBLine,distance):
    def CreateLine(point1,point2): # Take Revit.DB.Line by XYZ.Bisis
        line = Line.CreateBound(point1,point2)
        return line

    #0: End point , #1: StartPoint
    startPoint = [i.GetEndPoint(1) for i in lstDBLine]
    endPoint = [i.GetEndPoint(0) for i in lstDBLine]
    
    x_startPoint = [i.GetEndPoint(1).X for i in lstDBLine]
    y_startPoint = [i.GetEndPoint(1).Y for i in lstDBLine]
    z_startPoint = [i.GetEndPoint(1).Z for i in lstDBLine]
    x_endPoint = [i.GetEndPoint(0).X for i in lstDBLine]
    y_endPoint = [i.GetEndPoint(0).Y for i in lstDBLine]
    z_endPoint = [i.GetEndPoint(0).Z for i in lstDBLine]

    if round(x_startPoint[0]) == round(x_endPoint[0]):
        extend = -distance/304.8
        pxExStart = [i.Y - extend for i in startPoint]
        pxExEnd = [i.Y + extend for i in endPoint]

        y = pxExStart
        x = [i.X for i in startPoint]
        z = [i.Z for i in startPoint]
        p1 = [XYZ(x1,y1,z1) for x1,y1,z1 in zip(x,y,z)]

        y2 = pxExEnd
        x2 = [i.X for i in endPoint]
        z2 = [i.Z for i in endPoint]
        p2 = [XYZ(x2,y2,z2) for x2,y2,z2 in zip(x2,y2,z2)]
        return [CreateLine(i,j) for i,j in zip(p2,p1)]
        
    elif round(y_startPoint[0]) == round(y_endPoint[0]):
        extend = -distance/304.8
        pxExStart = [i.X - extend for i in startPoint]
        pxExEnd = [i.X + extend for i in endPoint]

        x = pxExStart
        y = [i.Y for i in startPoint]
        z = [i.Z for i in startPoint]
        p1 = [XYZ(x1,y1,z1) for x1,y1,z1 in zip(x,y,z)]

        x2 = pxExEnd
        y2 = [i.Y for i in endPoint]
        z2 = [i.Z for i in endPoint]
        p2 = [XYZ(x2,y2,z2) for x2,y2,z2 in zip(x2,y2,z2)]
        return [CreateLine(i,j) for i,j in zip(p2,p1)]

    elif round(z_startPoint[0]) != round(z_endPoint[0]):
        extend = -distance/304.8
        pxExStart = [i.Z - extend for i in startPoint]
        pxExEnd = [i.Z + extend for i in endPoint]

        y = pxExStart
        x = [i.X for i in startPoint]
        z = [i.Z for i in startPoint]
        p1 = [XYZ(x1,y1,z1) for x1,y1,z1 in zip(x,y,z)]

        y2 = pxExEnd
        x2 = [i.X for i in endPoint]
        z2 = [i.Z for i in endPoint]
        p2 = [XYZ(x2,y2,z2) for x2,y2,z2 in zip(x2,y2,z2)]
        return [CreateLine(i,j) for i,j in zip(p2,p1)]
    OUT = extendLine(IN[1],50000)

def CreateOffsetCurve(lstCurve,distance,direction): #Autodesk.Revit.DB Curve
    re = []
    for i in line:
        if direction == 'X': newvector = XYZ(1,0,0)
        if direction == 'Y': newvector = XYZ(0,1,0)
        if direction == 'Z': newvector = XYZ(0,0,1)
        re.append(i.CreateOffset(distance,newvector))
    return re
    OUT = CreateOffsetCurve(line,1,'Y')

def pointOffsetDirection (lstDBline, vtbasis, dis):
    
    dis = dis/304.8
    dirLine = [i.Direction  for i in lstDBline]
    # vtbasis = XYZ.BasisZ
    # perpendicular vector of (dirLine,vtbasis )
    perpeVt = [i.CrossProduct(vtbasis) for i in dirLine]

    startPoint = [i.GetEndPoint(1) for i in lstDBline]
    endPoint = [i.GetEndPoint(0) for i in lstDBline]

    start_pointOffset = [(i + dis*j) for i, j in zip(startPoint, perpeVt)]
    end_pointOffset = [(i + dis*j) for i, j in zip(endPoint, perpeVt)]

    return start_pointOffset, end_pointOffset
    #dbLine = IN[1]
    # vtbasis = XYZ.BasisZ

    # OUT = pointOffsetDirection(dbLine, vtbasis, 500)

def two_pointOffsetDirection (lstDBline, vtbasis, dis):
    
    dis = dis/304.8
    dirLine = [i.Direction  for i in lstDBline]
    # vtbasis = XYZ.BasisZ
    # perpendicular vector of (dirLine,vtbasis )
    perpeVt = [i.CrossProduct(vtbasis) for i in dirLine]

    startPoint = [i.GetEndPoint(1) for i in lstDBline]
    endPoint = [i.GetEndPoint(0) for i in lstDBline]

    right_start_pointOffset = [(i + dis*j) for i, j in zip(startPoint, perpeVt)]
    right_end_pointOffset = [(i + dis*j) for i, j in zip(endPoint, perpeVt)]

    left_start_pointOffset = [(i - dis*j) for i, j in zip(startPoint, perpeVt)]
    left_end_pointOffset = [(i - dis*j) for i, j in zip(endPoint, perpeVt)]
    return [right_start_pointOffset,right_end_pointOffset], [left_start_pointOffset, left_end_pointOffset]

    # dbLine = IN[1]
    # vtbasis = XYZ.BasisZ
    # OUT = two_pointOffsetDirection(dbLine, vtbasis, IN[2])
def pointOffsetbyPoint (lstXYZ, lstDirec, dis):
    dis = dis/304.8
    pointOffset = [(i + dis*j) for i, j in zip(lstXYZ, lstDirec)]
    return pointOffset
    # lstXYZ = IN[1]
    # lstDirec = [i.Direction for i in IN[3]]
    # OUT = pointOffsetbyPoint(lstXYZ, lstDirec, IN[2])

def middlePoint(lstDBline,parameter):
    # Evaluates and returns the point that matches a parameter along the curve.
    re = []
    for i in line:
        re.append(i.Evaluate(parameter,True))
    return re
    OUT = middlePoint(line,0.5)

def getEdgesAsCurveLoops(lstPlanar): # Get CurveLopps of PlanarFaces
    re = []
    for i in lstPlanar:
        re.append(i.GetEdgesAsCurveLoops())
    return re
    OUT = getEdgesAsCurveLoops(lstPlanar)

def getPlaneFromFlannarFace(lstPlanar):
    re = []
    for i in lstPlanar:
        re.append(i.GetSurface())
    return re
# =========================================   
	vsBB = BoundingBoxXYZ()
	vsBB.Transform = t
	vsBB.Min = vsBBmin
	vsBB.Max = vsBBmax

def centerPointbyDBLine(lstDBLine):
    starP = [i.GetEndPoint(1) for i in lstDBLine]
    endP = [i.GetEndPoint(0) for i in lstDBLine]
    cenP = [(i + j) / 2 for i, j in zip(starP, endP)]
    return cenP

def getPointByLine(references):
    endpoints = []
    for reference in references:
        element = doc.GetElement(reference.ElementId)
        curve = element.GeometryCurve
        start_point = curve.GetEndPoint(0)
        end_point = curve.GetEndPoint(1)
        endpoints.append([start_point, end_point])
    return endpoints
def get_pipe_endpoints(pipe_refs):
    endpoints = []
    for ref in pipe_refs:
        pipe = doc.GetElement(ref) # Get the pipe object from the reference
        location_curve = pipe.Location.Curve # Get the location curve of the pipe
        start_point = location_curve.GetEndPoint(0) # Get the start point
        end_point = location_curve.GetEndPoint(1) # Get the end point
        endpoints.append([start_point, end_point])
    return endpoints

def flatten_to_minimum_level(lst, level):
    def flatten_helper(items, curr_level):
        flattened = []
        for item in items:
            if curr_level < level and isinstance(item, list):
                flattened.extend(flatten_helper(item, curr_level + 1))
            else:
                flattened.append(item)
        return flattened

    return flatten_helper(lst, 1)

def logger(title, content):
    import datetime
    date = datetime.datetime.now()
    f = open(r"A:\Library-Dynamo-Python-CSharp\python.log", 'a')
    f.write(str(date) + '\n' + title + '\n' + str(content) + '\n')
    f.close()


def getValueByKeyObject(keys, objects):
    arrKeys, values = [], []
    for k in keys:
        if k in objects.keys():
            arrKeys.append(k)
            val =  str(objects[k])
            if val.isnumeric(): values.append(round(float(val),2))
            else: values.append(str(objects[k]))

    return arrKeys, values