"""Copyright by: duengocnguyen@gmail.com"""

import clr  # ​Common​ ​Language​ ​Runtime
            # This is .NET's Common Language Runtime.
import sys  #sys is a fundamental Python library - here
            #we're using it to load in the standard IronPython libraries

import System  #The System namespace at the root of .NET

clr.AddReference('ProtoGeometry') 
#A Dynamo library for its proxy geometry classes.
#You'll only need this if you're interacting with geometry.
from Autodesk.DesignScript.Geometry import *
#Loads everything in Dynamo's geometry library


clr.AddReference('RevitAPI') #Adding reference to Revit's API DLLs
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI') #Adding reference to Revit's API DLLs
from Autodesk.Revit.UI import *

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('RevitNodes') #Dynamo's nodes for Revit

import Revit #Loads in the Revit namespace in RevitNodes
clr.ImportExtensions(Revit.GeometryConversion) #You'll only need this if you're interacting with geometry.
clr.ImportExtensions(Revit.Elements) #More loading of Dynamo's Revit libraries
clr.AddReference('RevitServices')  #Dynamo's classes for handling Revit documents

import RevitServices
from RevitServices.Persistence import DocumentManager
#An internal Dynamo class
#that keeps track of the document that Dynamo is currently attached to

from RevitServices.Transactions import TransactionManager
#A Dynamo class for opening and closing transactions to change the Revit document's database

doc = DocumentManager.Instance.CurrentDBDocument # Take document currently
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument 
# link: https://help.autodesk.com/view/RVT/2021/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_html

"""----------------------------------------------------------------------------------"""

#Preparing input from dynamo to revit
element = UnwrapElement(IN[0])


"""
FilteredElementCollector(doc):Constructs a new FilteredElementCollector that will search and 
filter the set of elements in a document.
FilteredElementCollector Constructor (Document, ElementId): Constructs a new FilteredElementCollector that will search
and filter the visible elements in a view.
"""

"""________________________________________BASIC______________________"""
### Get all Element that are of the FamilyInstance class…
#____OfClass_____
ele_Lv = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType().ToElements();
el_Floor = FilteredElementCollector(doc).OfClass(Floor).WhereElementIsElementType().ToElements();
el_Wall = FilteredElementCollector(doc).OfClass(Wall).WhereElementIsNotElementType().ToElements();
el_Grid = FilteredElementCollector(doc).OfClass(Grid).WhereElementIsNotElementType().ToElements();


get_ElementType = FilteredElementCollector(doc).OfClass(ElementType).ToElements()
get_FamilyInstance_Actiview = FilteredElementCollector(doc).OfClass(FamilyInstance).ToElements();
get_AllFamily = FilteredElementCollector(doc).OfClass(Family).ToElements();

cads = FilteredElementCollector(doc).OfClass(ImportInstance).ToElements()
OUT = [i.LookupParameter("Name").AsString() for i in cads], [i.Id for i in cads] 


###Get all the Element that are of a BuiltInCategory…
#____BuiltInCategory…_____
ele_Wall1 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
ele_StrFraming = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
ele_StrColumn = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType().ToElements()
ele_Window = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()
ele_Door = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()

### Get all the Elements that are of a BuiltInCategory in the ActiveView Only…
ele_Wall = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
ele_StrFraming = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
ele_Floor = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()


###Get all the Elements that are of Class, BuiltInCategory and in the ActiveView Only…

ele_StrFraming =[FilteredElementCollector(doc, doc.ActiveView.Id).
                OfClass(FamilyInstance).OfCategory(BuiltInCategory.OST_StructuralFraming).
                WhereElementIsNotElementType().
                ToElements()]
ele_StrColumn =[FilteredElementCollector(doc, doc.ActiveView.Id).
                OfClass(FamilyInstance).OfCategory(BuiltInCategory.OST_StructuralColumns).
                WhereElementIsNotElementType().
                ToElements()]

"""________________________________________IMTERMEDIATE______________________"""
#ElementMulticlassFilter Example...
#Allows collector to collect Elements of Mulitple Classes...
 
#Build a new empty Type List...
typeList = List[System.Type]()
#Only Add some Element Types to TypeList...
typeList.Add(Floor)
typeList.Add(Wall)
typeList.Add(Level)
typeList.Add(Grid)

"""----------------------------ElementMulticlassFilter (takes a list of ElementTypes)...----------------"""
emcf = ElementMulticlassFilter(typeList)
#Collect all element that pass the ElementMulticlassFilter...
elems = FilteredElementCollector(doc).WherePasses(emcf).WhereElementIsNotElementType().ToElements()
OUT = elems


"""----------------------------ElementMultiCategoryFilter (takes a list of ElementTypes)...----------------"""
#Build a new empty Category List...
cate_List = List[BuiltInCategory]()
#Only Add some Element Types to cate_List...
cate_List.Add(BuiltInCategory.OST_StructuralFraming)
cate_List.Add(BuiltInCategory.OST_StructuralColumns)
cate_List.Add(BuiltInCategory.OST_StructuralFoundation)
cate_List.Add(BuiltInCategory.OST_Floors)
cate_List.Add(BuiltInCategory.OST_Walls)
cate_List.Add(BuiltInCategory.OST_Windows)
cate_List.Add(BuiltInCategory.OST_Doors)

_filter = ElementMulticategoryFilter(cate_List)
elems = FilteredElementCollector(doc).WherePasses(_filter).WhereElementIsNotElementType().ToElements()
OUT = elems




"""----------------------------ElementIsCurveDriven----------------------------"""
#Allows collector to collect Elements which are Curve Driven (e.g. beams, raking columns e.t.c.)...
#Create an ElementIsCurveDrivenFilter...
_filter1 = ElementIsCurveDrivenFilter()
#Collect all elements that pass the ElementIsCurveDrivenFilter...
elems = FilteredElementCollector(doc).WherePasses(_filter1).WhereElementIsNotElementType().ToElements()
OUT = elems


"""----------------------------ElementStructuralTypeFilter----------------------"""
#Allows collector to collect Elements of a StructuralType...

#Create a filter to get all Elements of the StructuralType of Footing... #Looking for at RevitLoopkup
_filter2 = ElementStructuralTypeFilter(Structure.StructuralType.Footing)
_filter3 = ElementStructuralTypeFilter(Structure.StructuralType.Column, True) # NOT of a StructuralType by using the Inverted Overload
_filter4 = ElementStructuralTypeFilter(Structure.StructuralType.Beam)
#Collect all elements that pass the ElementStructuralTypeFilter...
elems = FilteredElementCollector(doc).WherePasses(_filter3).WhereElementIsNotElementType().ToElements()
OUT = elems

"""----------------------------CurveElementFilter----------------------"""
#Allows collector to collect Elements of a CurveElementType...
#Create a filter that filters by CurveElementType ModelCurve...
_filter5 = CurveElementFilter(CurveElementType.ModelCurve)
#Collect all elements that pass the ElementStructuralTypeFilter...
elems = FilteredElementCollector(doc).WherePasses(_filter5).WhereElementIsNotElementType().ToElements()
OUT = elems

"""----------------------------ElementParameterFilter----------------------"""
#Allows collector to collect Elements with Parameter Values that pass filter rules...
#We will get all floors greater than 200mm thick...

#use the BuiltInParameter for floor thickness as the subject for the ParameterValueProvider...
vdoc = ParameterValueProvider(ElementId(BuiltInParameter.FLOOR_ATTR_DEFAULT_THICKNESS_PARAM))

#Tests whether numeric values from the document are greater than a certain value
reason = FilterNumericGreater()
#the certain value we want to test
v_Check = 200/304.8
#Create the rule with the above rules...
fRule = FilterDoubleRule(vdoc, reason, v_Check, 0.000001)
#create the ElementParameterFilter with the new rule...
_filter6 = ElementParameterFilter(fRule)
#Collect all the Elements that pass the ElementParameterFilter...
elems = FilteredElementCollector(doc).OfClass(Floor).WherePasses(_filter6).WhereElementIsNotElementType().ToElements()
OUT = elems


"""----------------------------SelectableInViewFilter----------------------"""
#Allows collector to collect Elements that are selectable in View...
 
#Create the SelectableInViewFilter (Requires you to Import the RevitAPIUI.dll)...
_filter7 = Selection.SelectableInViewFilter(doc,doc.ActiveView.Id)
#Collect all the Elements that pass the SelectableInViewFilter...
elems = FilteredElementCollector(doc).WherePasses(_filter7).WhereElementIsNotElementType().ToElements()
OUT = elems




"""----------------------------Sheet----------------------"""

viewcollector = FilteredElementCollector(doc).OfClass(View)

sheetcollector = FilteredElementCollector(doc).OfClass(ViewSheet)

collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).WhereElementIsElementType().ToElements()
OUT = FilteredElementCollector(doc).OfClass(Family).ToElements()

int(Sheet_Number_Begin[0]),




#https://forum.dynamobim.com/t/different-ways-of-getting-element-ids/7782/2
elems = FilteredElementCollector(doc, doc.ActiveView.Id)
re = List[Autodesk.Revit.DB.ElementId]()
for i in solB:
    re.Add(i.Id)
OUT = re