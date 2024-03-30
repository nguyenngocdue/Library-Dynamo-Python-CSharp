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
