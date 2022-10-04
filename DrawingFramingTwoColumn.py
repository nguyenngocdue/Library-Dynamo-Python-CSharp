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




doc = DocumentManager.Instance.CurrentDBDocument
curve = UnwrapElement(IN[0]) # Assuming input is a Curve
member_type = UnwrapElement(IN[2]) # Assuming a single Type is provided
symbol = member_type.Symbol # Assuming member_type is FamilyInstance
level = UnwrapElement(IN[1]) # Assuming single Level is provided
structural_type = member_type.StructuralType

TransactionManager.Instance.EnsureInTransaction(doc)
fa = doc.Create.NewFamilyInstance(curve, symbol, level, structural_type)
TransactionManager.Instance.TransactionTaskDone()

OUT = symbol