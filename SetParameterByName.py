import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes")
import Revit

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

def ConvertColor(element):
	return Autodesk.Revit.DB.Color(element.Red, element.Green, element.Blue)

def OverrideGraphics(element, color, fill):
	ogs = OverrideGraphicSettings()
	ogs.SetProjectionFillColor(color)
	ogs.SetCutFillColor(color)
	ogs.SetProjectionFillPatternId(fill.Id)
	ogs.SetCutFillPatternId(fill.Id)
	doc.ActiveView.SetElementOverrides(element.Id, ogs)

walls = UnwrapElement(IN[0])
newcolorlist = UnwrapElement(IN[1])
fillpat = UnwrapElement(IN[2])

for i in range(0, len(walls)):
  try:
	  TransactionManager.Instance.EnsureInTransaction(doc)
	  newcolor = ConvertColor(newcolorlist[i])
	  OverrideGraphics(walls[i], newcolor, fillpat)
	  TransactionManager.Instance.TransactionTaskDone()
  except:
    "Done"



