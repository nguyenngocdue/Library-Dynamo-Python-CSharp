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

###------------------------------------------------ Geometry Autocad ---------------------------------------------------------###

def getInstanceGeo(dwg): # getInstanceGeometry (DB(Line,PolyLine,Solid))
    geoIns = []
    for i in dwg.Geometry[ Options() ]:
        for j in i.GetInstanceGeometry():
            geoIns.append(j)
        return geoIns

def getLinesFromGeoIns(lstGeoIns):
    sol = []
    for i in lstGeoIns:
        if i.GetType() == Autodesk.Revit.DB.Line:
            sol.append(i)
    return sol

def getPolyLineFromGeoIns(lstGeoIns):
    sol = []
    for i in lstGeoIns:
        if i.GetType() == Autodesk.Revit.DB.PolyLine:
            sol.append(i)
    return sol

def getSolidFromGeoIns(lstGeoIns):
    sol = []
    for i in lstGeoIns:
        if i.GetType() == Autodesk.Revit.DB.Solid and i.SurfaceArea >0:
            sol.append(i)
        elif i.GetType() == GeometryInstance:
            var = i.SymbolGeometry
            sol.append([i.SurfaceArea > 0 for i in var])
    return sol
    # get_InstanGeo = IN[1]
    # get_SolidFromGeoIns = [getSolidFromGeoIns(i) for i in get_InstanGeo]
    # OUT = get_SolidFromGeoIns
def getPlanarFormSolid(solids): # Get Planarface from solids
    plaf = []
    for i in solids:
        plaf.append(i.Faces)
    return plaf
    
def RetrieveEdgesFace(lstPlanar): # Get Lines of PlanarFaces
    re = []
    for t in lstPlanar:
        for j in t.EdgeLoops:
            re.append(i.AsCurve() for i in j)
    return re

def getLineMin(lstLine): # Get a min line of list line
    _length = []
    for i in lstLine:
        _length.append(i.Length)
    for j in lstLine:
        if j.Length == min(_length):
            return j
           # OUT = [GetLineMin(i) for i in IN[1]]  

def lstFlattenL2(list): #List.Flatten
    result = []
    for i in list:
        for j in i:
            result.append(j)
    return result

def getGraphicsStyleId(lstPlanar): # Get GraphicsStyleid
    re = []
    for t in lstPlanar:
        re.append(t.GraphicsStyleId)
    return re
def getGraphicsStyleCategory(lstId): # Get GraphicsStyleCategory
    grapStyCate = []
    grapSty = []
    doc = DocumentManager.Instance.CurrentDBDocument
    for t in lstId:
        grapSty.append(doc.GetElement(t))
    for j in grapSty:
        grapStyCate.append(j.GraphicsStyleCategory.Name)
    return grapStyCate

def getGraphicsStyleCategory(lstId): # Get GraphicsStyleCategory, grapStyCate, sortId
    grapStyCate = []
    grapSty = []
    sortId = []
    doc = DocumentManager.Instance.CurrentDBDocument
    for t in lstId:
        grapSty.append(doc.GetElement(t))
    try:
        for j in grapSty:
            if j.GraphicsStyleCategory.Name != "0":
                grapStyCate.append(j.GraphicsStyleCategory.Name)
                sortId.append(j.GraphicsStyleCategory.Id)

    except:
        "None"
    return grapStyCate, sortId


def getCurveShortLong(allCurve): # Get Short Curve in list Curve
    len_curveShort = []
    len_curveLong = []
    curveShort = []
    curveLong = []


    if allCurve.Count == 4:
        if allCurve[0].Length > allCurve[1].Length:
            len_curveShort.append(round(allCurve[1].Length*304.8))
            len_curveLong.append(round(allCurve[0].Length*304.8))
            curveShort.append(allCurve[1])
            curveLong.append(allCurve[0])


        else:
            len_curveShort.append(round(allCurve[0].Length*304.8))
            len_curveLong.append(round(allCurve[1].Length*304.8))
            curveShort.append(allCurve[0])
            curveLong.append(allCurve[1])
    else: 
        return len_curveShort.append("Not Items")
    return len_curveShort,len_curveLong

def getIndexOfList(lst,index): # Get a Value from Level 3 of a list by Index Number
    re = []
    for i in lst:
        c = i[index]
        re.append(c)
    return re

def nameFamily(lstNa1):
    re = []
    for n1 in lstNa1:
        v = str(n1).replace("mm","")
        v = v.replace(" ","")
        v = v.split("x")
        re.append(v)
    return re

def setdata(items,params,values):
	for i,param_name in enumerate(params):
		for elem in items: 
			param = elem.LookupParameter(param_name)
			if param == None:
				param = elem.Document.GetElement(elem.GetTypeId()).LookupParameter(param_name)
			if param.StorageType == StorageType.Double:
				param.Set(UnitUtils.ConvertToInternalUnits(values[i],param.DisplayUnitType))
			elif param.StorageType == StorageType.ElementId:
				param.Set(values[i].Id)
			else:
				param.Set(values[i])
		return param

###------------------------------------------------ Family ---------------------------------------------------------###
def getFamilyByCateString(CateString):
    doc = DocumentManager.Instance.CurrentDBDocument
    fiAllFamilyType = FilteredElementCollector(doc).OfClass(FamilySymbol).WhereElementIsElementType().ToElements();
    getType = [i for i in fiAllFamilyType if i.Category.Name == CateString]
    fa = [i.Family for i in getType ]
    family = list(set(fa))
    return family
    OUT = getFamilyByCateString("Structural Columns")

def getFamilyType(eleFA):
  doc = DocumentManager.Instance.CurrentDBDocument
  faTy = [doc.GetElement(i.GetTypeId()) for i in eleFA]
  return faTy

def duplicateFamilyType(lstFamtype,lstDupnames):
    result = []
    famtype = UnwrapElement(lstFamtype)
    for s in lstDupnames:
        try:
	        TransactionManager.Instance.EnsureInTransaction(doc)
	        newsymbol = [i.Duplicate(s) for i in lstFamtype]
	        result.Add(i.ToDSType(True) for i in newsymbol)
	        TransactionManager.Instance.TransactionTaskDone()
        except:
            " No Element"
    return result
    OUT = duplicateFamilyType(famtype,dupnames)

def nameFamily(lstNa1, lstNa2):
    re = []
    for n1,n2 in zip(lstNa1,lstNa2):
        v = str(n1).replace(".0","") + "x" + str(n2).replace(".0"," mm")
        re.append(v)
    return re
    OUT = nameFamily(IN[1],IN[2])

def FamilyInstanceByPointAndLevel(familyType,XYZpoint,level):
    re = [] 
    for i,j in zip(familyType,XYZpoint):
	    TransactionManager.Instance.EnsureInTransaction(doc)
	    re.append(doc.Create.NewFamilyInstance(j,i,level,Autodesk.Revit.DB.Structure.StructuralType.Column))
	    TransactionManager.Instance.TransactionTaskDone()
    return re

def getFamilySymboIds(family):
    id = [i.GetFamilySymbolIds() for i in family]
    return id

def familyTypesFrom_Family(family):
    family_type_ids = [i.GetFamilySymbolIds() for i in family]
    family_types = [doc.GetElement(id) for i in family_type_ids for id in i ]
    return family_types
    OUT = family_Types(UnwrapElement(IN[0]))

def familyTypesFrom_FamilyInstamce(familyInstance):
    family_types = [doc.GetElement(i.GetTypeId()) for i in familyInstance]
    return family_types
    OUT = familyTypesFrom_FamilyInstamce(UnwrapElement(IN[0]))

def familyInstanceFrom_Family(family):
	doc = DocumentManager.Instance.CurrentDBDocument
    family_type_ids = [i.GetFamilySymbolIds() for i in family]
  	family_instances = []  
	for family_type_id in family_type_ids:
        family_instance_filter = FamilyInstanceFilter(doc, family_type_id)
		elements = FilteredElementCollector(doc).WherePasses(family_instance_filter).ToElements()
		family_instances.append(elements)
    return family_instances
    #OUT = familyInstanceFrom_Family(UnwrapElement(IN[0]))

def familyInstanceFrom_Family(family):
    doc = DocumentManager.Instance.CurrentDBDocument
    family_type_ids = [i.GetFamilySymbolIds() for i in family]
    family_instances = []  
    for family_type_id in family_type_ids:
        for j in family_type_id:
            family_instance_filter = FamilyInstanceFilter(doc, j)
            elements = FilteredElementCollector(doc).WherePasses(family_instance_filter).ToElements()
            family_instances.append(elements)
    return family_instances
    #OUT = familyInstanceFrom_Family(UnwrapElement(IN[0]))

# ele =UnwrapElement(IN[0])
# OUT=LayersInImportInstance(ele)
# """Filter Family"""
# fams = FilteredElementCollector(doc).OfClass(Family).ToElements()
# """Filter FamilyType"""
# famTypes = FilteredElementCollector(doc).OfClass(FamilySymbol).ToElements()
# """Category From Family"""
# for fam in families:
# categoryFromFamity=categories.append(Revit.Elements.Category.ById(fam.FamilyCategoryId.IntegerValue))


###------------------------------------------------ getElementFromAutocad ---------------------------------------------------------###
def LayersInImportInstance(obj):
	clr.AddReference("DSCoreNodes")
	import DSCore
	layerCad=[]
	cat=obj.Category.SubCategories.GetEnumerator()
	while cat.MoveNext():
		layerCad.append(cat.Current.Name)
	return DSCore.List.Sort(layerCad)

