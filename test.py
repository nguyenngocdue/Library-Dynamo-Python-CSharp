# import clr 
# import System
# import math 
# from System.Collections.Generic import *


# clr.AddReference('RevitAPI')
# import Autodesk
# from Autodesk.Revit.DB import *

# clr.AddReference('RevitAPIUI')
# from Autodesk.Revit.UI import*
# from  Autodesk.Revit.UI.Selection import*

# clr.AddReference("RevitNodes")
# import Revit
# clr.ImportExtensions(Revit.Elements)
# clr.ImportExtensions(Revit.GeometryConversion)

# clr.AddReference("ProtoGeometry")
# from Autodesk.DesignScript.Geometry import *

# clr.AddReference("RevitServices")
# import RevitServices
# from RevitServices.Persistence import DocumentManager
# from RevitServices.Transactions import TransactionManager


# #########################################################################
# def getList(inputValue):
#     if isinstance(inputValue, list):
#         return UnwrapElement(inputValue)
#     else:
#         return [UnwrapElement(inputValue)]
# elements = getList(IN[1]) 
# #########################################################################
# doc = DocumentManager.Instance.CurrentDBDocument
# view = doc.ActiveView
# uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
# #########################################################################


# # objects = FilteredElementCollector(doc).OfClass(Family).ToElements()

# # OUT = [obj.Name for obj in objects]
# # OUT = [obj.LookupParameter("Name").AsString() for obj in objects]

# # of Category 
# # objects = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()

# # OUT = objects

# #build a new empty type list
# # typeList = List[System.Type]()

# # typeList.Add(Floor)
# # typeList.Add(Wall)
# # typeList.Add(Level)
# # typeList.Add(Grid)

# # emcf = ElementMulticlassFilter(typeList)
# # elements = FilteredElementCollector(doc).WherePasses(emcf).WhereElementIsNotElementType().ToElements()
# # OUT = emcf

# # cateLst = List[BuiltInCategory]()

# # cateLst.Add(BuiltInCategory.OST_StructuralFraming)
# # cateLst.Add(BuiltInCategory.OST_StructuralColumns)
# # cateLst.Add(BuiltInCategory.OST_StructuralFoundation)
# # cateLst.Add(BuiltInCategory.OST_Floors)
# # cateLst.Add(BuiltInCategory.OST_Walls)
# # cateLst.Add(BuiltInCategory.OST_Doors)

# # filters = ElementMulticategoryFilter(cateLst)
# # elements = FilteredElementCollector(doc).WherePasses(filters).WhereElementIsNotElementType().ToElements()

# # OUT = elements

# pvp = ParameterValueProvider(ElementId(BuiltInParameter.FLOOR_ATTR_DEFAULT_THICKNESS_PARAM))
# #
# fnrv = FilterNumericGreater();
# ruleValue = 200/304.8

# fRule =  FilterDoubleRule(pvp, fnrv, ruleValue, 0.000001)
# filters = ElementParameterFilter(fRule)

# elements = FilteredElementCollector(doc).WherePasses(filters).WhereElementIsNotElementType().ToElements()

# OUT = elements

print(132)