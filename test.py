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
pipeTypes = IN[1]
systemTypes = IN[2]
levels = IN[3]
diameters = IN[4]

if isinstance(lines, list):
    lines = lines
else:
    lines = [lines]

if isinstance(pipeTypes, list):
    pipeTypes = UnwrapElement(pipeTypes)
else:
    pipeTypes = [UnwrapElement(pipeTypes)]
lenPipeType = len(pipeTypes)


if isinstance(systemTypes, list):
    systemTypes = UnwrapElement(systemTypes)
else:
    systemTypes = [UnwrapElement(systemTypes)]
lenSystemType = len(systemTypes)

if isinstance(levels, list):
    levels = UnwrapElement(levels)
else:
    levels = [UnwrapElement(levels)]
lenLevel = len(levels)

if isinstance(diameters, list):
    diameters = diameters
else:
    diameters = [diameters]
diaLen = len(diameters)


firstPoints = [x.StartPoint for x in lines]
secondPoints = [x.EndPoint for x in lines]

pipes = []
TransactionManager.Instance.EnsureInTransaction(doc)
for index, point in enumerate(firstPoints):
    try:
        systemTypeId = systemTypes[index%lenSystemType].Id
        pipeTypeId = pipeTypes[index%lenPipeType].Id
        levelId = levels[index%lenLevel].Id
        diam = diameters[index%diaLen]
        pipe = Autodesk.Revit.DB.Plumbing.Pipe.Create(doc, systemTypeId, pipeTypeId, levelId, point.ToXyz(),secondPoints[index].ToXyz())
        param = pipe.get_Parameter(BuiltInParameter.RBS_PIPE_DIAMETER_PARAM)
        param.SetValueString(diam.ToString())
        
        pipes.append(pipe.ToDSType(False))
    except:
        pipes.append(None)
TransactionManager.Instance.TransactionTaskDone()
OUT = pipes
