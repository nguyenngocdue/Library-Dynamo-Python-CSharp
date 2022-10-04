#----------------------------------------------------------------
# Get all of BuiltInParameter
builtInParams = System.Enum.GetValues(BuiltInParameter)

#----------------------------------GetLevel--------------------------------:
#Preparing input from dynamo to revit
fa = UnwrapElement(IN[1])
re =[]
elevation = []
for ref in fa:
    TransactionManager.Instance.EnsureInTransaction(doc)
    varb = ref.Host
    re.append(varb)
    try:
    	elevation.append(varb.Elevation*304.8)
    except:
    	"Cann't change"
    TransactionManager.Instance.TransactionTaskDone()
OUT = re,elevation


#--------------------------------Reference Level - Elevation----------------------------------------------------
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

#Inspired by Clockwork
def GetLevel(item):
	val = None
	if hasattr(item, "LevelId"): 
		val = item.Document.GetElement(item.LevelId)
		if val: return val
	if hasattr(item, "Level"):
		val = item.Level
		if val: return val
	if hasattr(item, "GenLevel"):
		val = item.GenLevel
		if val: return val
	if (item.GetType().ToString() in ("Autodesk.Revit.DB.Architecture.StairsRun", "Autodesk.Revit.DB.Architecture.StairsLanding")):
		item = item.GetStairs()
	if (item.GetType().ToString() == "Autodesk.Revit.DB.Architecture.Stairs") or item.Category.Id == ElementId(BuiltInCategory.OST_Ramps):
		try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.STAIRS_BASE_LEVEL_PARAM).AsElementId())
		except: pass
	if (item.GetType().ToString() == "Autodesk.Revit.DB.ExtrusionRoof"):
		try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.ROOF_CONSTRAINT_LEVEL_PARAM).AsElementId())
		except: pass
	if (item.GetType().ToString() == "Autodesk.Revit.DB.Mechanical.Duct" or "Autodesk.Revit.DB.Electrical.Conduit"):
		try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.RBS_START_LEVEL_PARAM).AsElementId())
		except: pass
	if hasattr(item, "OwnerViewId"):
		view = item.Document.GetElement(item.OwnerViewId)
		if hasattr(view, "GenLevel"):
			val = view.GenLevel
			if val: return val
	if not val:
		try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_REFERENCE_LEVEL_PARAM).AsElementId())
		except: 
			try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM).AsElementId())
			except: 
				try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.SCHEDULE_LEVEL_PARAM).AsElementId())
				except:
					#if item is work plane based
					collector = FilteredElementCollector(item.Document).OfClass(Level).ToElements()
					try: return [level for level in collector if item.get_Parameter(BuiltInParameter.SKETCH_PLANE_PARAM).AsString().split(": ")[-1] == level.Name][0]
					except: return None

ProcessLists = lambda function, lists: [ProcessLists(function, item) if isinstance(item, list) else function(item) for item in lists]
ApplyFunction = lambda func, objs: ProcessLists(func, objs) if isinstance(objs, list) else [func(objs)]

def Unwrap(item):
    return UnwrapElement(item)
    
if isinstance(IN[0], list):
	items = ProcessLists(Unwrap, IN[0])
else:
	items = Unwrap(IN[0])

lv =ApplyFunction(GetLevel,items)
elevation = []
for i in lv:
	elevation.append(i.Elevation*304.8)
OUT = lv , elevation


