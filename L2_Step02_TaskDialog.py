import clr
import msvcrt
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*

checkRun  = IN[1]
content  = IN[2]
result = str(content)

#btn = TaskDialogCommonButtons.Close
btn = TaskDialogCommonButtons.Ok
#btn = TaskDialogCommonButtons.None
if checkRun == True:
    TaskDialog.Show('Result',"Your value is: "+ result, btn)
else:
    " Welcome to my dynamo course \n Set True To Run"

OUT = result