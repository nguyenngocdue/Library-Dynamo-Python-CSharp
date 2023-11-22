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
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms.DataVisualization')
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
#View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

#########################################################################


#########################################################################
elements = IN[1]

def getGeoElement(element): # Get geometry of element.
    geo = []
    opt = Options()
    opt.View = doc.ActiveView
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    geoByElement = element.get_Geometry(opt)
    return geoByElement


lstEle = UnwrapElement(IN[1])
if isinstance(lstEle,list):
    elements = UnwrapElement(lstEle)
else:
    elements = [UnwrapElement(lstEle)]
    

        
OUT = [getGeoElement(i) for i in elements]
