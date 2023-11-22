# Import libraries
import sys
import clr

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import System Enum
import System
from System.Collections.Generic import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Transactions import TransactionManager
from RevitServices.Persistence import DocumentManager

# Define Current Document
doc = DocumentManager.Instance.CurrentDBDocument

# /// This is where the fun starts ///
# INPUT
schedule = UnwrapElement(IN[0])
# or input1 = UnwrapElement(IN[0])

# CODE
s_def = schedule.Definition

# TRANSACTION
TransactionManager.Instance.EnsureInTransaction(doc)

s_def.AddField(ScheduleFieldType.Formula)

TransactionManager.Instance.TransactionTaskDone()

# OUTPUT
OUT = s_def
