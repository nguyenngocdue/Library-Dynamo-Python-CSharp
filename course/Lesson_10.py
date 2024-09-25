import clr 
import System
import math 
from System.Collections.Generic import *
import json

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*
from System import Enum

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from Autodesk.Revit.DB import BuiltInCategory
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
from  Autodesk.Revit.UI.Selection import ISelectionFilter
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


#########################################################################
def getList(inputValue):
	if isinstance(inputValue, list):
		return UnwrapElement(inputValue)
	else:
		return [UnwrapElement(inputValue)]
elements = getList(IN[1]) 
#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#########################################################################

class SelectionFilter(ISelectionFilter):
	def __init__(self, categoryInputs):
		self.category_names = categoryInputs
	def AllowElement(self, element):
		return element.Category.Name in self.category_names
	def AllowReference(self, ref, xyz):
		return False


def classifyElementsByCategoies(uidoc, cateNames, prompt):
	selectionFilters = SelectionFilter(cateNames)
	elements = uidoc.Selection.PickElementsByRectangle(selectionFilters, prompt)
	cateElements = {}
	for element in elements: 
		cateName = element.Category.Name
		if cateName not in cateElements: cateElements[cateName] = []
		cateElements[cateName].append(element)
	return cateElements


import json
filePath = r"U:\17_TrainingAdvanceDynamo\K02\Scripts\config_tool.json"
with open(filePath, 'r') as file:
	data = json.load(file)

categoryNames = []
for obj in data.values():
	for item in obj.values():
		category = item['category']
		categoryNames.append(category)

OUT = classifyElementsByCategoies(uidoc, categoryNames, "Select elemets")