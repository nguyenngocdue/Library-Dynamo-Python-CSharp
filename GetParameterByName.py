import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *



doc = DocumentManager.Instance.CurrentDBDocument
fa = UnwrapElement(IN[1])

"""_______________________________________________________Set List For Items_______________________"""
if isinstance(IN[1],list):
    fa = UnwrapElement(IN[1])
else:
    fa = [UnwrapElement(IN[1])]

"""_________________________________________________________WAY 1___________________________________"""
getFamilyType = []
for i in fa:
    getId = i.GetTypeId()
    getFamilyType.append(doc.GetElement(getId))
OUT = getFamilyType

getAllPara = []
getAllNamePara = []
getTypePara = []
getValPara = []
for j in getFamilyType:
    allPara = j.Parameters # has it name?
    for k in allPara:
        # Get Name of Para
         namePara = k.Definition.Name 
         getAllNamePara.append(namePara)
        # Get Type Of Para
         typePara = k.Definition.ParameterType 
         getTypePara.append(typePara)
        # Get Value Of Para
         if k.Definition.Name == IN[2]: 
             var = k.AsDouble()*304.8
             getValPara.append(var)             
OUT = getValPara

"""_________________________________________________________WAY 2_____________________________________"""
valPara = []
getFamilyType = [doc.GetElement(i.GetTypeId()) for i in fa]
getPara = [i.Parameters for i in getFamilyType] 
getValPara = [i.LookupParameter(IN[2]).AsDouble()*304.8 for i in getFamilyType] # Run LookupParameter from getFamilyType not into SetParateres
OUT = getValPara

"""___________________________________Design - Def GetParameterByName__________________________________"""
def GetParameterByName(lstEle,para):
    doc = DocumentManager.Instance.CurrentDBDocument
    if isinstance(lstEle,list):
        element = UnwrapElement(lstEle)
    else:
        element = [UnwrapElement(lstEle)]
    TransactionManager.Instance.EnsureInTransaction(doc)
    valPara = []
    valPara.append(i.LookupParameter(para).AsDouble()*304.8 for i in [doc.GetElement(i.GetTypeId()) for i in element])
    TransactionManager.Instance.TransactionTaskDone()
    return valPara
OUT = GetParameterByName(IN[1],IN[2])



def GetParameterValue(parameter):
  value= None
  if parameter.StorageType == StorageType.Double:
    value =  parameter.AsDouble()
  elif parameter.StorageType == StorageType.Integer:
    if parameter.Definition.ParameterType == ParameterType.Integer:
      value = parameter.AsInteger()
    else:
      value = parameter.AsValueString()
  elif parameter.StorageType == StorageType.String:
    value = parameter.AsString()
  elif parameter.StorageType == StorageType.ElementId:
    value = parameter.AsElementId()
  return value

  
