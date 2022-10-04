import clr #This is .NET's Common Language Runtime. It's an execution environment
#that is able to execute code from several different languages.

import sys #sys is a fundamental Python library - here, we're using it to load in
#the standard IronPython libraries
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib') #Imports the
#standard IronPython libraries, which cover everything from servers and
#encryption through to regular expressions.


import System #The System namespace at the root of .NET

from System import Array #.NET class for handling array information

from System.Collections.Generic import * #Lets you handle generics. Revit's API
#sometimes wants hard-typed 'generic' lists, called ILists. If you don't need
#these you can delete this line.
clr.AddReference('ProtoGeometry')  #A Dynamo library for its proxy geometry
#classes. You'll only need this if you're interacting with geometry.


from Autodesk.DesignScript.Geometry import * #Loads everything in Dynamo's
#geometry library
clr.AddReference("RevitNodes") #Dynamo's nodes for Revit

import Revit #Loads in the Revit namespace in RevitNodes
clr.ImportExtensions(Revit.Elements) #More loading of Dynamo's Revit libraries
clr.ImportExtensions(Revit.GeometryConversion) #More loading of Dynamo's
#Revit libraries. You'll only need this if you're interacting with geometry.
clr.AddReference("RevitServices") #Dynamo's classes for handling Revit documents

import RevitServices 
from RevitServices.Persistence import DocumentManager #An internal Dynamo class
#that keeps track of the document that Dynamo is currently attached to
from RevitServices.Transactions import TransactionManager #A Dynamo class for
#opening and closing transactions to change the Revit document's database
clr.AddReference("RevitAPI") #Adding reference to Revit's API DLLs
clr.AddReference("RevitAPIUI") #Adding reference to Revit's API DLLs

import Autodesk #Loads the Autodesk namespace
from Autodesk.Revit.DB import * #Loading Revit's API classes
from Autodesk.Revit.UI import * #Loading Revit's API UI classes  

doc = DocumentManager.Instance.CurrentDBDocument #Finally, setting up handles to the active Revit document
uiapp = DocumentManager.Instance.CurrentUIApplication #Setting a handle to the active Revit UI document
app = uiapp.Application  #Setting a handle to the currently-open instance of the Revit application
uidoc = uiapp.ActiveUIDocument #Setting a handle to the currently-open instance of the Revit UI application
#######OK NOW YOU CAN CODE########

OUT = True