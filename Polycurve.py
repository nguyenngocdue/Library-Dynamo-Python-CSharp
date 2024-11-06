# Copyright and other metadata provided
"""Copyright(c) 2023 by: duengocnguyen@gmail.com
site_url: https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g
repository_url:https://github.com/nguyenngocdue/Library-Dynamo-Python-CSharp
________________Welcome to BIM3DM-DYNAMO API___________________"""

# Import necessary CLR and system libraries for .NET integration
import clr
import System
import math
from System.Collections.Generic import *

# Import ProtoGeometry for Dynamo geometric operations
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

# Add references to access Revit API functionalities
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# Import RevitNodes to interact with Revit elements more efficiently
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# Import RevitServices for accessing the document and transactions
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Initialize the document and UI document objects
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
view = doc.ActiveView

# Function to convert Dynamo lines to Revit database lines
def getDbLineFromLine(lstLine):
    """Convert a list of Dynamo lines to Revit DB Lines using Dynamo's conversion methods."""
    re = []
    for i in lstLine:
        # Convert Dynamo line to Revit Curve
        revitCurve = i.ToRevitType()
        re.append(revitCurve)
    return re

# Main execution block
lines = UnwrapElement(IN[1])  # Unwrap the Dynamo elements to access Revit elements
dbLines = getDbLineFromLine(lines)  # Convert unwrapped lines to Revit DB lines

from Autodesk.DesignScript.Geometry import PolyCurve, Line
polyCurve = PolyCurve.ByJoinedCurves(lines)
OUT = polyCurve