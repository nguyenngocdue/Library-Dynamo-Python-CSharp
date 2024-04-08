"""Copyright(c) 2023 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

################################################################
lines = IN[0]
pipeType = IN[1]
systemType = IN[2]
level = IN[3]
diameter = IN[4]

if isinstance(lines, list):
    lines = lines
else:
    lines = [lines]
firstPoints = [x.StartPoint for x in lines]
secondPoints = [x.EndPoint for x in lines]


if isinstance(pipeType, list):
    pipeType = UnwrapElement(pipeType)
else:
    pipeType = [UnwrapElement(pipeType)]
pipeLen = len(pipeType)




if isinstance(systemType, list):
    systemType = UnwrapElement(systemType)
else:
    systemType = [UnwrapElement(systemType)]
sysLen = len(systemType)

if isinstance(level, list):
    level = UnwrapElement(level)
else:
    level = [UnwrapElement(level)]
diaLevel = len(level)

if isinstance(diameter, list):
    diameter = diameter
else:
    diameter = [diameter]
diaLen = len(diameter)

elements = []

TransactionManager.Instance.EnsureInTransaction(doc)
for index,point in enumerate(firstPoints):
    try:
        levelId = level[index%diaLevel].Id
        sysTypeId = systemType[index%sysLen].Id
        pipeTypeid = pipeType[index%pipeLen].Id
        diam = diameter[index%diaLen]
        pipe = Autodesk.Revit.DB.Plumbing.Pipe.Create(doc,sysTypeId,pipeTypeid,levelId,point.ToXyz(),secondPoints[index].ToXyz())
        param = pipe.get_Parameter(BuiltInParameter.RBS_PIPE_DIAMETER_PARAM)
        param.SetValueString(diam.ToString())
        elements.append(pipe.ToDSType(False))	
    except:
        elements.append(None)
TransactionManager.Instance.TransactionTaskDone()


OUT = elements


"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
# 'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
sys.path.append(r'C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\2.10')
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

# Preparing input from Dynamo to Revit
elements1 = UnwrapElement(IN[0])

# Do some action in a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Find intersections between elements
result = []
for elem1, elem2 in zip(elements1, elements1):
    intersection_points = [] 
    for e1 in elem1:
        for e2 in elem2:
            intersections = e1.Intersect(e2)
            for i in intersections:
                if hasattr(i, 'X') and i.X is not None:
                    intersection_points.append(i)
    result.append(intersection_points)
TransactionManager.Instance.TransactionTaskDone()

# Output the intersection points
OUT = result
