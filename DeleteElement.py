import clr
import sys
import System
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

from System.Collections.Generic import List

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

toList = lambda x : x if hasattr(x, '__iter__') else [x]

lst_elements = toList(UnwrapElement(IN[0]))
lst_elementIds = List[ElementId]([x.Id for x in lst_elements])

TransactionManager.Instance.EnsureInTransaction(doc)
doc.Delete(lst_elementIds)
TransactionManager.Instance.TransactionTaskDone()

OUT = lst_elementIds