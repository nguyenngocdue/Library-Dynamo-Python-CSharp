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
#######################################################################################
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
DB = Autodesk.Revit.DB

#######################################################################################

def get_sheets(include_placeholders=True, include_noappear=True, doc=None):
	doc = DocumentManager.Instance.CurrentDBDocument
    	sheets = list(DB.FilteredElementCollector(doc)
                  .OfCategory(DB.BuiltInCategory.OST_Sheets)
                  .WhereElementIsNotElementType())
    	if not include_noappear:
        	sheets = [x for x in sheets
                  if x.Parameter[DB.BuiltInParameter.SHEET_SCHEDULED]
                  .AsInteger() > 0]
    	if not include_placeholders:
        	return [x for x in sheets if not x.IsPlaceholder]

    	return sheets
    ###OUT = get_sheets()

def get_doc_categories(doc=None, include_subcats=True):
    doc = DocumentManager.Instance.CurrentDBDocument
    all_cats = []
    cats = doc.Settings.Categories
    all_cats.extend(cats)
    if include_subcats:
        for cat in cats:
            all_cats.extend([x for x in cat.SubCategories])
    return all_cats

def get_schedule_categories(doc=None):
    doc = doc
    all_cats = get_doc_categories(doc)
    cats = []
    for cat_id in DB.ViewSchedule.GetValidCategoriesForSchedule():
        for cat in all_cats:
            if cat.Id.IntegerValue == cat_id.IntegerValue:
                cats.append(cat)
    #OUT = get_schedule_categories()

def get_all_linkeddocs(doc=None):
    doc =  DocumentManager.Instance.CurrentDBDocument
    linkinstances = DB.FilteredElementCollector(doc)\
                      .OfClass(DB.RevitLinkInstance)\
                      .ToElements()
    docs = [x.GetLinkDocument() for x in linkinstances]
    return [x for x in docs if x]
    #OUT = get_all_linkeddocs()

def get_all_grids(doc=None):
    doc =  DocumentManager.Instance.CurrentDBDocument
    target_docs = [doc]
    all_grids = []
    for tdoc in target_docs:
        if tdoc is not None:
            all_grids.extend(list(
                DB.FilteredElementCollector(tdoc)
                .OfCategory(DB.BuiltInCategory.OST_Grids)
                .WhereElementIsNotElementType()
                .ToElements()
                ))
    return all_grids
    #OUT = get_all_linkeddocs()

def get_param(element, param_name, default=None):
    
    if isinstance(element, DB.Element):
        try:
            return element.LookupParameter(param_name)
        except Exception:
            return default


