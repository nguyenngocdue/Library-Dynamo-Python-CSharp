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

################### Definitions ###################
def tolist(obj1):
	if hasattr(obj1,"__iter__"): return obj1
	else: return [obj1]
################### Inputs ###################

sheet =UnwrapElement(IN[1])
view = UnwrapElement(IN[2])
#point = [tolist(IN[3])]*len(view)
point = UnwrapElement(IN[3]*len(view))

re = []
   

for x,y,l in zip(sheet,view,point):
    TransactionManager.Instance.EnsureInTransaction(doc) 
    re.append(Autodesk.Revit.DB.Viewport.Create(doc,x.Id,y.Id,l.ToXyz()))
    TransactionManager.Instance.TransactionTaskDone()        
OUT = re

