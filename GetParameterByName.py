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
def getParameterByName(lstEle,para):
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



def getParameterValue(parameter):
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
################################################################
################################################################
################################################################
################################################################
"""Copyright(c) 2023 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
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
from Autodesk.Revit.DB.Structure import *

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
from Autodesk.DesignScript.Geometry import Point


path_to_check = r'C:\Users\NGUYEN NGOC DUE\AppData\Roaming\Dynamo\Dynamo Revit\2.10\packages\packages\BIM3DM\lib'
import sys
sys.path.append(path_to_check)
#########################################################################
def is_array(obj):
    return "List" in obj.__class__.__name__ or "list" in obj.__class__.__name__ 

def get_array_rank(array):
    if is_array(array):
        return 1 + max(get_array_rank(item) for item in array)
    else:
        return 0
def flatten_to_1d(arr):
    result = []
    def recursive_flatten(subarray):
        for item in subarray:
            if is_array(item):
                recursive_flatten(item)
            else:
                result.append(item)

    recursive_flatten(arr)
    return result
def returnOUT(fn, objects):
    rank = get_array_rank(objects)
    if rank == 0:  # a
        return fn(objects)
    elif rank == 1:  # [a]
        return [fn(*args) for args in objects]
    elif rank == 2:  # [[a]]
        return [fn(*i) for i in objects for i in j]
    else:
        elements = flatten_to_1d(objects)  # [a]
        return fn(elements)


#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
app  = uidoc.Application
DB = Autodesk.Revit.DB
############################### FUNCTION #################################
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
def logPython(title, content):
    import datetime
    date = datetime.datetime.now()
    f = open(r"A:\Library-Dynamo-Python-CSharp\python.log", 'a')
    f.write(str(date) + '\n' + title + '\n' + str(content) + '\n')
    f.close()

def getValuesByParams(lstEle,paramNames, isShowAll=False):
    doc = DocumentManager.Instance.CurrentDBDocument
    allValues, paramNamesEle = [], []
    elements = UnwrapElement(lstEle)
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

############################### INPUT #################################
objects = UnwrapElement(IN[0])
rank = get_array_rank(objects)
objects = objects if rank else [objects]
############################### OUTPUT ##################################

OUT = getValuesByParams(objects, ['b', 'h'], True)
################################################################
################################################################
################################################################
################################################################

  
