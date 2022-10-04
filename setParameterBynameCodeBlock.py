"
elements = IN[0]
val = IN[1]
try:
	for e,v in zip(elements,val):
		e.SetParameterByName('Top Constraint',v)
		OUT = 'done';
except:
	OUT = 'Not';
";


#----------------------------------------------------------------

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import System	

elements = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
parameter_names = UnwrapElement(IN[1]) if isinstance(IN[1],list) else [UnwrapElement(IN[1])]
values = UnwrapElement(IN[2]) if isinstance(IN[2],list) else [UnwrapElement(IN[2])]
def setdata(elements,params,values):
	re = []
	doc = DocumentManager.Instance.CurrentDBDocument
	for i, param_name in enumerate(params):
		for elem in elements:
			param =  elem.LookupParameter(param_name)
			if param == None:
				param = elem.Document.GetElement(elem.GetTypeId()).LookupParameter(param_name)
			if param.StorageType == StorageType.ElementId:
				TransactionManager.Instance.EnsureInTransaction(doc) 
				param.Set(values[i].Id)
				TransactionManager.Instance.TransactionTaskDone()

			elif param.StorageType == StorageType.Double:
				TransactionManager.Instance.EnsureInTransaction(doc) 
				param.Set(UnitUtils.ConvertToInternalUnits(values[i],param.DisplayUnitType))
				TransactionManager.Instance.TransactionTaskDone()
			else:
				TransactionManager.Instance.EnsureInTransaction(doc) 
				param.Set(values[i])
				TransactionManager.Instance.TransactionTaskDone()
			re.append(elem)
	return re
OUT = setdata(elements,parameter_names,values)


#----------------------------------------------------------------
import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import System	

elements = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
parameter_names = UnwrapElement(IN[1]) if isinstance(IN[1],list) else [UnwrapElement(IN[1])]
values = UnwrapElement(IN[2]) if isinstance(IN[2],list) else [UnwrapElement(IN[2])]
inputdocs = UnwrapElement(IN[3]) if isinstance(IN[3],list) else [UnwrapElement(IN[3])]
inputdoc=inputdocs[0]

#Part of script from Clockwork
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument

def setdata(items,params,values):
	for i,param_name in enumerate(params):
		for elem in items: 
			param = elem.LookupParameter(param_name)
			if param == None:
				param = elem.Document.GetElement(elem.GetTypeId()).LookupParameter(param_name)
			if param.StorageType == StorageType.Double:
				param.Set(UnitUtils.ConvertToInternalUnits(values[i],param.DisplayUnitType))
			elif param.StorageType == StorageType.ElementId:
				param.Set(values[i].Id)
			else:
				param.Set(values[i])
		return items

try:
	TransactionManager.Instance.ForceCloseTransaction()
	t = Transaction(doc,'Set')
	t.Start()
	data=setdata(elements,parameter_names,values)
	t.Commit()      
	OUT = data, doc

except:
    # if error accurs anywhere in the process catch it
    import traceback
    errorReport = traceback.format_exc()
    OUT = errorReport


#----------------------------------------------------------------
import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import System	

elements = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
parameter_names = UnwrapElement(IN[1]) if isinstance(IN[1],list) else [UnwrapElement(IN[1])]
values =IN[2]
inputdocs = UnwrapElement(IN[3]) if isinstance(IN[3],list) else [UnwrapElement(IN[3])]
inputdoc=inputdocs[0]

#Part of script from Clockwork
if inputdoc == None:
	doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
	doc = inputdoc
else: doc = DocumentManager.Instance.CurrentDBDocument

def setdata(elements,values):
	re = []
	check = []
	try: 
		for elem,val in zip(elements, values):
			TransactionManager.Instance.EnsureInTransaction(doc) 
			param = elem.LookupParameter("Top Constraint").Set(val.Id)
			TransactionManager.Instance.TransactionTaskDone()
			re.append(elem)
			check.append(param)
	except:
		"Can't Change"
	return re

OUT = setdata(elements,values)