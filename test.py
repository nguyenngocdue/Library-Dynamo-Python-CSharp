"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
import clr 
import System
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
from Autodesk.DesignScript.Geometry import Line, Point
from Autodesk.DesignScript.Geometry import GeometryExtension

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
from Autodesk.Revit.DB.Structure import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
import math
import random

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
################################################################

import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import FilteredElementCollector, ViewSchedule, ScheduleFieldType, ScheduleFieldId, SectionType, Transaction

# Assuming that 'doc' is defined elsewhere in your script as the current document

def addColumnToSchedule(schedule, column_name):
    # Get the existing fields
    schedule_fields = schedule.Definition.GetSchedulableFields()
    # Find the SchedulableField by name
    emptyField = []
    for field in schedule_fields:
        if field.GetName(doc) == column_name:
            schedulable_field = field
            try:
                TransactionManager.Instance.EnsureInTransaction(doc)
                schedule.Definition.AddField(schedulable_field)
                TransactionManager.Instance.TransactionTaskDone()
            except:
                emptyField.append(column_name)
    return "'" +  ', '.join(emptyField) + "'" + 'fields is included in Schedule'
        

# Example usage
schedule = UnwrapElement(IN[0])
column_name = UnwrapElement(IN[1])

OUT = [addColumnToSchedule(schedule, i) for i in column_name]






