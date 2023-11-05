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
import math
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
################################################################

# Define a function to get rebar style id based on the style name
def GetRebarStyleId(styleName):
    category = BuiltInCategory.OST_RebarTags
    rebarStyles = FilteredElementCollector(doc).OfCategory(category).ToElements()
    for style in rebarStyles:
        name_param = style.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
        if name_param and name_param.AsString() == styleName:
            return style.Id
    return None

rebarStyle = 'Standard'
# Check the input rebar style and get its id
if rebarStyle == "Standard":
    rebarStyleId = GetRebarStyleId("Standard")
elif rebarStyle == "Stirrup":
    rebarStyleId = GetRebarStyleId("Stirrup")
else:
    rebarStyleId = None

# Create an output list with rebar host element and rebar style id
OUT = [rebarHost, rebarStyleId]
