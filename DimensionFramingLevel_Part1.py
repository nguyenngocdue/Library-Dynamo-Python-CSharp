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

def pickObjectsFilter(filter):
	el_ref = uidoc.Selection.PickObjects(ObjectType.Element, filter)
	typelist = list()
	for i in el_ref:
		try:
			typelist.append(doc.GetElement(i.ElementId))
		except:
			typelist.apped(list())
	return typelist		

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
###--------------------------------------- Step 1 -------------------------------###

ele = SelectionFilter("Structural Framing", "Levels")
elSelectAll = pickObjectsFilter(ele)
OUT = elSelectAll

###--------------------------------------- Step 2 -------------------------------###
level = []
eleFraming = []
for i in elSelectAll:
    if i.Category.Name == "Levels": level.append(i)
    if i.Category.Name == "Structural Framing": eleFraming.append(i)
OUT =  level, eleFraming

###--------------------------------------- Step 3 -------------------------------###
getGeoFraming = [GetGeoElement(i) for i in eleFraming]
OUT = getGeoFraming

getSolidFraming = [GetSolidFromGeo(i) for i in getGeoFraming]
OUT = [j.ToProtoType() for i in getSolidFraming for j in i]

getPlanrFraming = [GetPlanarFormSolid(i) for i in getSolidFraming]
OUT = getPlanrFraming ,getSolidFraming