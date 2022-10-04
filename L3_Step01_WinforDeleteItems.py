import clr
import System
 
from System.Collections.Generic import*

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import*

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*

# Khai báo tài liệu sử dụng
doc = DocumentManager.Instance.CurrentDBDocument # take Element Current View
view = doc.ActiveView # take Current View

nameLevel = []

####################################################################################################################
lvs = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType().ToElements()
# Why is ToElements?, Why is doc variable in FilteredElementCollector, How to use search Revit .html
# Autodesk.Revit.DB.Level => You need to change it become to Element.
####################################################################################################################

#* Way 1 : It can get error when you change computer
# for i in lvs:
#     var = i.ToDSType(True) # Change method of Element to Dynamo environment.
#     nameLevel.append(var.Name)

#* Way 2
# for i in lvs:
#     var = Element.Name.__get__(i)
#     nameLevel.append(i)

#* Way 3
# nameLevel = [Element.Name.__get__(x) for x in lvs]

####################################################################################################################

# Taake Element of Family Type in entire project
fTypeFilter = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsElementType(). ToElements()
#Take Elements in Current View
fInstanceFilter = FilteredElementCollector(doc,view.Id).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()

####################################################################################################################


#OUT = doc, view
#OUT = lvs, nameLevel
#OUT =  nameLevel
OUT = fTypeFilter ,fInstanceFilter

