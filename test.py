import clr
import System
 
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
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import Selection
from  Autodesk.Revit.UI.Selection import ISelectionFilter

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
#########################################################################
def is_array(obj):
    return "List" in obj.__class__.__name__
def get_array_rank(array):
    if is_array(array):
        return 1 + max(get_array_rank(item) for item in array)
    else:
        return 0
def flatten_to_1d(arr):
    result = []
    def recursive_flatten(subarray):
        for item in subarray:
            if is_array(item):
                recursive_flatten(item)
            else:
                result.append(item)

    recursive_flatten(arr)
    return result

#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#########################################################################



def getFamilyByOfCategory(OST_cateNane):
	collector = FilteredElementCollector(doc).OfCategory(OST_cateNane).OfClass(Family).ToElements()
	return collector, OST_cateNane

objects = UnwrapElement(IN[1])
rank = get_array_rank(objects)
if rank == 0:
    OUT = getFamilyByOfCategory(objects)
elif rank == 1:
    OUT = [getFamilyByOfCategory(element) for element in objects]
else:
    elements = flatten_to_1d(objects)
    OUT = getFamilyByOfCategory(objects)