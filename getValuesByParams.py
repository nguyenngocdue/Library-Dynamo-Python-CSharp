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
            if not parameter.AsDouble(): return "empty value"
            else: return parameter.AsDouble()*304.84
        elif parameter.StorageType == StorageType.String:
            if not parameter.AsString(): return "empty value"
            else: return parameter.AsString()
        else:
            return "" 
    else:
        return None
def logger(title, content):
    import datetime
    date = datetime.datetime.now()
    f = open(r"A:\Library-Dynamo-Python-CSharp\python.log", 'a')
    f.write(str(date) + '\n' + title + '\n' + str(content) + '\n')
    f.close()

def getValuesByParams(lstEle,paramNames, isShowAll=False):
    doc = DocumentManager.Instance.CurrentDBDocument
    allValues, paramNamesEle = [], []
    if isinstance(lstEle,list):
        elements = UnwrapElement(lstEle)
    else:
        elements = [UnwrapElement(lstEle)]
    for ele in elements:
        familyType = doc.GetElement(ele.GetTypeId())
        allParams = familyType.Parameters
        allNamePrams = [p.Definition.Name for p in allParams]
        result = {}
        for name in paramNames:
            valueOfParam = getParameterValueFromLookup(ele, name)
            if not isShowAll:
                if valueOfParam:
                    result[name] = valueOfParam
                    paramNamesEle.append(name)
                else:
                    for p in allParams:
                        for name in paramNames:
                            if p.Definition.Name == name:
                                result[name] = getParameterValue(p)
                                paramNamesEle.append(name)
            else:
                if valueOfParam and isShowAll:
                    result[name] = valueOfParam
                    paramNamesEle.append(name)
                if not valueOfParam and isShowAll:
                    for p in allParams:
                        result[p.Definition.Name] = getParameterValue(p)
                        # for name in paramNames:
                        #     if p.Definition.Name == name:
                        #         result[name] = getParameterValue(p)
                        #         paramNamesEle.append(name)
               
        paramNamesEle = list(set(paramNamesEle + allNamePrams))
        diffNamesEle = diffArrays(paramNames, paramNamesEle)

        result['id'] = ele.Id
        allValues.append(result)
        
    return allValues, listToDict(diffNamesEle)
    
fa = IN[0]
paramOnProperties = IN[2]

OUT = getValuesByParams(fa,paramOnProperties, IN[1])