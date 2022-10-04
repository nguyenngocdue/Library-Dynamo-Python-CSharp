import clr
import msvcrt
clr.AddReference("RevitAPIUI")
from  Autodesk.Revit.UI import *

msg = str(IN[0])
amount = len(IN[0])

button = TaskDialogCommonButtons.Ok
result = TaskDialogResult.Ok
msgBox = TaskDialog
if msg != None:
    OUT = msgBox.Show("Filter Null Element - NNDUE","Count: "+ str(amount)+ " Family ____" + msg +"____" " is Null "+ "=>>Import That Family, Please! "+"🐶🐶🐶", button) 
else:
    OUT = msgBox.Show("Filter Null Element - NNDUE", "Everything is OKEY", button) 