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
# clr.AddReference('System.Windows.Forms.DataVisualization')
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
#########################################################################
doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._Schedules = System.Windows.Forms.GroupBox()
		self._lstSche = System.Windows.Forms.ListBox()
		self._rdbtAll = System.Windows.Forms.RadioButton()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._bttExport = System.Windows.Forms.Button()
		self._bttCancel = System.Windows.Forms.Button()
		self._Schedules.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# Schedules
		# 
		self._Schedules.Controls.Add(self._rdbtAll)
		self._Schedules.Controls.Add(self._lstSche)
		self._Schedules.Location = System.Drawing.Point(14, 13)
		self._Schedules.Name = "Schedules"
		self._Schedules.Size = System.Drawing.Size(467, 154)
		self._Schedules.TabIndex = 0
		self._Schedules.TabStop = False
		self._Schedules.Text = "Schedules"
		# 
		# lstSche
		# 
		self._lstSche.FormattingEnabled = True
		self._lstSche.Location = System.Drawing.Point(6, 19)
		self._lstSche.Name = "lstSche"
		self._lstSche.Size = System.Drawing.Size(453, 108)
		self._lstSche.TabIndex = 0
		# 
		# rdbtAll
		# 
		self._rdbtAll.Location = System.Drawing.Point(7, 127)
		self._rdbtAll.Name = "rdbtAll"
		self._rdbtAll.Size = System.Drawing.Size(104, 24)
		self._rdbtAll.TabIndex = 1
		self._rdbtAll.TabStop = True
		self._rdbtAll.Text = "Check All/None"
		self._rdbtAll.UseVisualStyleBackColor = True
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._button1)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(14, 175)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(467, 55)
		self._groupBox1.TabIndex = 1
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Export Options"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Output folder:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(80, 20)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(298, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(384, 20)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "Browse..."
		self._button1.UseVisualStyleBackColor = True
		# 
		# bttExport
		# 
		self._bttExport.Location = System.Drawing.Point(317, 236)
		self._bttExport.Name = "bttExport"
		self._bttExport.Size = System.Drawing.Size(75, 23)
		self._bttExport.TabIndex = 2
		self._bttExport.Text = "Export"
		self._bttExport.UseVisualStyleBackColor = True
		# 
		# bttCancel
		# 
		self._bttCancel.Location = System.Drawing.Point(398, 236)
		self._bttCancel.Name = "bttCancel"
		self._bttCancel.Size = System.Drawing.Size(75, 23)
		self._bttCancel.TabIndex = 3
		self._bttCancel.Text = "Cacel"
		self._bttCancel.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self.ClientSize = System.Drawing.Size(495, 264)
		self.Controls.Add(self._bttCancel)
		self.Controls.Add(self._bttExport)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._Schedules)
		self.Name = "MainForm"
		self.ShowIcon = False
		self.Text = "Export Schedule Dynamo Winform"
		self._Schedules.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


form  = MainForm()
Application.Run(form)

OUT = 0