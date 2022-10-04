import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Form, Button, Label, TextBox
doc = __revit__.ActiveUIDocument.Document

def createView ( sender, event): # creates drafting view
	viewTypes = list(FilteredElementCollector(doc).OfClass(ViewFamilyType))
	for vt in viewTypes:
		if str(vt.ViewFamily) == 'Drafting':
			viewType = vt
			break
	t = Transaction (doc, 'Make new Drafting view')
	t.Start()

	newDraftingView = ViewDrafting.Create(doc, viewType.Id)
	newDraftingView.Name = textBox.Text

	t.Commit()

	status.Text = 'Drafting View created!'
	
# create Windows form
form = Form()
form.Width = 300
form.Height = 145
# Title text
label = Label()
label.Text = "New Drafting View name"
label.Width = 280
label.Parent = form
# User input
textBox = TextBox()
textBox.Text = "Enter View Name here"
textBox.Width = 280
textBox.Top += 25
textBox.Parent = form
# Button to action
button = Button()
button.Text = "Create View"
button.Click += createView
button.Width = 280
button.Top += 50
button.Parent = form
# Title text
status = Label()
status.Text = ""

status.Width = 280
status.Top += 75
status.Parent = form
form.ShowDialog()

