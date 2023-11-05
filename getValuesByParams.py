"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
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
import math
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument


def getParameterValue(parameter):
  value= None
  if parameter.StorageType == StorageType.Double:
    value =  parameter.AsDouble()*304.84
  elif parameter.StorageType == StorageType.Integer:
    if parameter.Definition.ParameterType == ParameterType.Integer:
      value = parameter.AsInteger()*304.84
    else:
      value = parameter.AsValueString()
  elif parameter.StorageType == StorageType.String:
    value = parameter.AsString()
  elif parameter.StorageType == StorageType.ElementId:
    value = parameter.AsElementId()
  return value

def diffArrays(arr1, arr2):
    diff = []
    for item in arr1:
        if item not in arr2:
            diff.append(item)
    return diff

def listToDict(lst):
    dictionary = {}
    for index, item in enumerate(lst):
        dictionary[str(index)] = str(item)
    return dictionary

def getParameterValueFromLookup(element, parameter_name):
    parameter = element.LookupParameter(parameter_name)
    if parameter is not None and parameter.HasValue:
        if parameter.StorageType == StorageType.Double:
            return parameter.AsDouble()*304.84
        elif parameter.StorageType == StorageType.String:
            return parameter.AsString()
        else:
            return "" 
    else:
        return None

def getValuesByParams(lstEle,paramNames, showAll=False):
    doc = DocumentManager.Instance.CurrentDBDocument
    allValues, paramUndefine, paramNamesEle = [], [], []
    if isinstance(lstEle,list):
        elements = UnwrapElement(lstEle)
    else:
        elements = [UnwrapElement(lstEle)]
    for ele in elements:
        result = {}
        for name in paramNames:
            parameter = ele.LookupParameter(name)
            if not parameter or showAll:
                familyType = doc.GetElement(ele.GetTypeId())
                allParams = familyType.Parameters
                paramNamesEle = paramNamesEle + [p.Definition.Name for p in allParams]
                for p in allParams:
                    if showAll:
                        result[p.Definition.Name] = getParameterValue(p)
                    else:
                        for name in paramNames:
                            if p.Definition.Name == name:
                                result[name] = getParameterValue(p)
            if parameter or showAll:
                valueOfParam = getParameterValueFromLookup(ele, name)
                result[name] = valueOfParam
                paramNamesEle.append(name)
        result['id'] = ele.Id
        allValues.append(result)
        paramUndefine.append(listToDict(diffArrays(paramNames, paramNamesEle)))
    return allValues, paramUndefine
    
fa = IN[0]
paramOnProperties = IN[1]

OUT = getValuesByParams(fa,paramOnProperties, IN[2])