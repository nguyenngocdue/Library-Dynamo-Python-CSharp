"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
__doc__ = '.........'
__author__ = 'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
__title__ = '.....'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
sys.path.append(r'C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\IronPython.StdLib.2.7.8')
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

sheetnames = IN[0]
sheetNumber = IN[1]
titleblock = UnwrapElement(IN[2])
sheetlist = list()


TransactionManager.Instance.EnsureInTransaction(doc)

for number in range(len(sheetnames)):
  newsheet = ViewSheet.Create(doc,titleblock.Id)
  newsheet.Name = sheetnames[number]
  newsheet.SheetNumber = sheetNumber[number]
  sheetlist.append(newsheet.ToDSType(False))

TransactionManager.Instance.TransactionTaskDone()

OUT = sheetlist