import clr
import System
 
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import*
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import Selection
from  Autodesk.Revit.UI.Selection import ISelectionFilter

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
#########################################################################
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms.DataVisualization')
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

#########################################################################


class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listView1 = System.Windows.Forms.ListView()
		self._cbbx = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listView1
		# 
		self._listView1.Location = System.Drawing.Point(5, 54)
		self._listView1.Name = "listView1"
		self._listView1.Size = System.Drawing.Size(366, 339)
		self._listView1.TabIndex = 0
		self._listView1.UseCompatibleStateImageBehavior = False
		# 
		# cbbx
		# 
		self._cbbx.FormattingEnabled = True
		self._cbbx.Location = System.Drawing.Point(5, 27)
		self._cbbx.Name = "cbbx"
		self._cbbx.Size = System.Drawing.Size(366, 21)
		self._cbbx.TabIndex = 1
		self._cbbx.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		self._cbbx.Items.AddRange(System.Array[System.Object](["a", "b", "c", "d"]))

		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(204, 399)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "Cancel"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(285, 399)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "Ok"
		self._button2.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.AllowDrop = True
		self.AutoScroll = True
		self.AutoSize = True
		self.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink
		self.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self.ClientSize = System.Drawing.Size(382, 425)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._cbbx)
		self.Controls.Add(self._listView1)
		self.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
		self.HelpButton = True
		self.Name = "MainForm"
		self.ShowIcon = False
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Form"
		self.TopMost = True
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
			pass

	def ComboBox1SelectedIndexChanged(self, sender, e):
		selected_item = self._cbbx.SelectedItem

		if selected_item == "a":
			self.UpdateListView(0, 10)
		elif selected_item == "b":
			self.UpdateListView(11, 20)
		elif selected_item == "c":
			self.UpdateListView(21, 30)
		elif selected_item == "d":
			self.UpdateListView(50, 100)
			pass

	def UpdateListView(self, start, end):
		self._listView1.Items.Clear()
		data = System.Array[object]([str(i) for i in range(start, end + 1)])
		for item in data:
			self._listView1.Items.Add(item)




Application.Run(MainForm())