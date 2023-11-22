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
self._cbbFil.Items.AddRange(System.Array[System.Object](filStatus))
self._cbbx.Items.AddRange(System.Array[System.Object](["a", "b", "c", "d"]))





#################################Link_Click########################################
class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._linkLabel1 = System.Windows.Forms.LinkLabel()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(339, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g"
		self._label1.Click += self.Link_Click
		# 
		# linkLabel1
		# 
		self._linkLabel1.Location = System.Drawing.Point(13, 36)
		self._linkLabel1.Name = "linkLabel1"
		self._linkLabel1.Size = System.Drawing.Size(338, 23)
		self._linkLabel1.TabIndex = 1
		self._linkLabel1.TabStop = True
		self._linkLabel1.Text = "https://www.facebook.com/groups/864660200378936"
		self._linkLabel1.LinkClicked += self.LinkLabel1LinkClicked
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(666, 316)
		self.Controls.Add(self._linkLabel1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "bb"
		self.ResumeLayout(False)

	def Link_Click(self, sender, e):
		System.Diagnostics.Process.Start(self._label1.Text)
		pass
	def LinkLabel1LinkClicked(self, sender, e):
		System.Diagnostics.Process.Start(self._linkLabel1.Text)
		
Application.Run(MainForm())


# CheckBox:
	def ChbWFlCheckedChanged(self, sender, e):
		self.Selected = []
		if self._chbWFl.CheckedChanged != None:
			self.Selected.append(IN[1])
			self.Close()
		pass
