__title__ = "BIM3DM"  # Name of the button displayed in Revit UI
#========================================================================
import clr
clr.AddReference("System")   
import System
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import*
from Autodesk.Revit.DB import Transaction, FilteredElementCollector
from pyrevit import revit, forms
from System.Collections.Generic import List
from pyrevit import revit, DB, UI, HOST_APP, forms


clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
# from  Autodesk.Revit.UI.Selection import*

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

import math 
from System.Collections.Generic import *
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

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
from Autodesk.DesignScript.Geometry import Point

from rpw.ui.forms import (FlexForm, Label, ComboBox, Separator, Button, TextBox)
from collections import OrderedDict
from pyrevit.framework import List
from Autodesk.Revit import Exceptions
import sys

#========================================================================
from pyrevit import forms
#========================================================================
doc = __revit__.ActiveUIDocument.Document # Document class from RevitAPI that represents project.
uidoc = __revit__.ActiveUIDocument # UIDocument class from RevitAPI that represents Revit project opened in the Revit UI.
app = __revit__.Application # Represents the Autodesk Revit Application, providing.
view = revit.active_view
#########################################################################
class SelectionFilter(ISelectionFilter):
	def __init__(self, ctgName1):
		self.ctgName1 = ctgName1

	def AllowElement(self, element):
		if element.Category.Name == self.ctgName1:
			return True
		else:
			return False
#########################################################################
ele = SelectionFilter("Text Notes")
elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")



#########################################################################


txt_types = FilteredElementCollector(doc).OfClass(TextNoteType)
text_style_dict= {txt_t.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString(): txt_t for txt_t in txt_types}

components = [
	Label("Pick Text Style"),
	ComboBox(name="textstyle_combobox", options=text_style_dict),
	Label("Middle Sign"),
	TextBox(name="middle_sign", Text=""),
	Label("Begin Number"),
	TextBox(name="number", Text="1"),
	Button("Select")
	]

form = FlexForm("Select", components)
ok = form.show()
if ok:
	# assign chosen values
	text_style = form.values["textstyle_combobox"]
	middle_sign = form.values["middle_sign"]
	number = int(form.values["number"])
else:
	sys.exit()


condition = True
n = number
try:
	while condition:
		with Transaction(doc, __title__) as t:
			t.Start("Create Grid")
			pickPoint = uidoc.Selection.PickPoint("Select Point")
			text = str(elSelectAll[0].Text) + str(middle_sign) + str(n)
			text_without_newline = text.replace("\r", "")
			# print(text_without_newline)
			text_note = DB.TextNote.Create(doc, view.Id, pickPoint, text_without_newline , text_style.Id)
			n = n + 1
			t.Commit()
except Exception as e:
	condition = False
	str(e)