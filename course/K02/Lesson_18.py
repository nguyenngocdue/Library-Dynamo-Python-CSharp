"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
sys.path.append(r'A:\Library-Dynamo-Python-CSharp')
import math 
from System.Collections.Generic import *

from DynamoVN import *


clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*
from  Autodesk.Revit.UI.Selection import ISelectionFilter
import os
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
#############################################################################
def getList(inputValue):
	if isinstance(inputValue, list):
		return UnwrapElement(inputValue)
	else:
		return [UnwrapElement(inputValue)]
#############################################################################
elements = getList(IN[0])
username = os.getlogin()
defaulExtPath = rf'C:\Users\{username}\AppData\Roaming\pyRevit\Extensions\pyBIM3DM.extension\pyBIM3DM.tab'
typeSource = ['.py', '.dyn', '.dll']

columns = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType().ToElements()

################################################################
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._txtb_ext_tab_path = System.Windows.Forms.TextBox()
		self._btn_ext_tab_path = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._btn_icon_path = System.Windows.Forms.Button()
		self._txtb_panel_name = System.Windows.Forms.TextBox()
		self._txtb_btn_name = System.Windows.Forms.TextBox()
		self._txtb_icon_path = System.Windows.Forms.TextBox()
		self._btn_ok = System.Windows.Forms.Button()
		self._btn_cancel = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._cbbx_sel_file = System.Windows.Forms.ComboBox()
		self._txtb_file_path = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(21, 21)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(119, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Extension Tab:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# txtb_ext_tab_path
		# 
		self._txtb_ext_tab_path.Location = System.Drawing.Point(146, 23)
		self._txtb_ext_tab_path.Name = "txtb_ext_tab_path"
		self._txtb_ext_tab_path.Size = System.Drawing.Size(511, 20)
		self._txtb_ext_tab_path.TabIndex = 1
		self._txtb_ext_tab_path.Text = defaulExtPath
		# 
		# btn_ext_tab_path
		# 
		self._btn_ext_tab_path.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._btn_ext_tab_path.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
		self._btn_ext_tab_path.Cursor = System.Windows.Forms.Cursors.Hand
		self._btn_ext_tab_path.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._btn_ext_tab_path.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btn_ext_tab_path.ForeColor = System.Drawing.SystemColors.ControlText
		self._btn_ext_tab_path.Location = System.Drawing.Point(678, 21)
		self._btn_ext_tab_path.Name = "btn_ext_tab_path"
		self._btn_ext_tab_path.Size = System.Drawing.Size(102, 23)
		self._btn_ext_tab_path.TabIndex = 2
		self._btn_ext_tab_path.Text = "Browse ..."
		self._btn_ext_tab_path.UseVisualStyleBackColor = False
		self._btn_ext_tab_path.Click += self.Btn_ext_tab_pathClick
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Tahoma", 9.75)
		self._label2.Location = System.Drawing.Point(34, 22)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(94, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Panel Name:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Tahoma", 9.75)
		self._label3.Location = System.Drawing.Point(354, 22)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(87, 23)
		self._label3.TabIndex = 0
		self._label3.Text = "Button Name:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Tahoma", 9.75)
		self._label4.Location = System.Drawing.Point(34, 28)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(87, 23)
		self._label4.TabIndex = 0
		self._label4.Text = "Select a File:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Tahoma", 9.75)
		self._label5.Location = System.Drawing.Point(34, 29)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(87, 23)
		self._label5.TabIndex = 0
		self._label5.Text = "Icon Path:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# btn_icon_path
		# 
		self._btn_icon_path.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._btn_icon_path.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
		self._btn_icon_path.Cursor = System.Windows.Forms.Cursors.Hand
		self._btn_icon_path.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._btn_icon_path.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btn_icon_path.ForeColor = System.Drawing.SystemColors.ControlText
		self._btn_icon_path.Location = System.Drawing.Point(666, 29)
		self._btn_icon_path.Name = "btn_icon_path"
		self._btn_icon_path.Size = System.Drawing.Size(102, 23)
		self._btn_icon_path.TabIndex = 2
		self._btn_icon_path.Text = "Browse ..."
		self._btn_icon_path.UseVisualStyleBackColor = False
		self._btn_icon_path.Click += self.Btn_icon_pathClick
		# 
		# txtb_panel_name
		# 
		self._txtb_panel_name.Location = System.Drawing.Point(134, 22)
		self._txtb_panel_name.Name = "txtb_panel_name"
		self._txtb_panel_name.Size = System.Drawing.Size(198, 23)
		self._txtb_panel_name.TabIndex = 3
		# 
		# txtb_btn_name
		# 
		self._txtb_btn_name.Location = System.Drawing.Point(447, 22)
		self._txtb_btn_name.Name = "txtb_btn_name"
		self._txtb_btn_name.Size = System.Drawing.Size(198, 23)
		self._txtb_btn_name.TabIndex = 3
		# 
		# txtb_icon_path
		# 
		self._txtb_icon_path.Location = System.Drawing.Point(134, 29)
		self._txtb_icon_path.Name = "txtb_icon_path"
		self._txtb_icon_path.Size = System.Drawing.Size(511, 23)
		self._txtb_icon_path.TabIndex = 3
		# 
		# btn_ok
		# 
		self._btn_ok.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btn_ok.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
		self._btn_ok.Cursor = System.Windows.Forms.Cursors.Hand
		self._btn_ok.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._btn_ok.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btn_ok.ForeColor = System.Drawing.SystemColors.ControlText
		self._btn_ok.Location = System.Drawing.Point(678, 350)
		self._btn_ok.Name = "btn_ok"
		self._btn_ok.Size = System.Drawing.Size(102, 23)
		self._btn_ok.TabIndex = 2
		self._btn_ok.Text = "OK"
		self._btn_ok.UseVisualStyleBackColor = False
		self._btn_ok.Click += self.Btn_okClick
		# 
		# btn_cancel
		# 
		self._btn_cancel.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btn_cancel.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
		self._btn_cancel.Cursor = System.Windows.Forms.Cursors.Hand
		self._btn_cancel.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._btn_cancel.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btn_cancel.ForeColor = System.Drawing.SystemColors.ControlText
		self._btn_cancel.Location = System.Drawing.Point(555, 350)
		self._btn_cancel.Name = "btn_cancel"
		self._btn_cancel.Size = System.Drawing.Size(102, 23)
		self._btn_cancel.TabIndex = 2
		self._btn_cancel.Text = "Cancel"
		self._btn_cancel.UseVisualStyleBackColor = False
		self._btn_cancel.Click += self.Btn_cancelClick
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._txtb_btn_name)
		self._groupBox1.Controls.Add(self._txtb_panel_name)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 66)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(792, 66)
		self._groupBox1.TabIndex = 4
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Button"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._cbbx_sel_file)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Controls.Add(self._txtb_file_path)
		self._groupBox2.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold)
		self._groupBox2.Location = System.Drawing.Point(12, 153)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(792, 97)
		self._groupBox2.TabIndex = 5
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Source"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._label5)
		self._groupBox3.Controls.Add(self._txtb_icon_path)
		self._groupBox3.Controls.Add(self._btn_icon_path)
		self._groupBox3.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Bold)
		self._groupBox3.Location = System.Drawing.Point(12, 271)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(792, 63)
		self._groupBox3.TabIndex = 6
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Icon"
		# 
		# cbbx_sel_file
		# 
		self._cbbx_sel_file.FormattingEnabled = True
		self._cbbx_sel_file.Location = System.Drawing.Point(134, 28)
		self._cbbx_sel_file.Name = "cbbx_sel_file"
		self._cbbx_sel_file.Size = System.Drawing.Size(198, 24)
		self._cbbx_sel_file.TabIndex = 1
		self._cbbx_sel_file.SelectedIndexChanged += self.Cbbx_sel_fileSelectedIndexChanged
		self._cbbx_sel_file.Items.AddRange(System.Array[System.Object](typeSource))
		self._cbbx_sel_file.SelectedIndex = 0
		# 
		# txtb_file_path
		# 
		self._txtb_file_path.Location = System.Drawing.Point(134, 58)
		self._txtb_file_path.Name = "txtb_file_path"
		self._txtb_file_path.Size = System.Drawing.Size(511, 23)
		self._txtb_file_path.TabIndex = 1
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self.ClientSize = System.Drawing.Size(816, 385)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._btn_cancel)
		self.Controls.Add(self._btn_ok)
		self.Controls.Add(self._btn_ext_tab_path)
		self.Controls.Add(self._txtb_ext_tab_path)
		self.Controls.Add(self._label1)
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "MainForm"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Revit Tool Setup"
		self.TopMost = True
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox2.PerformLayout()
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()

	def Btn_ext_tab_pathClick(self, sender, e):
		dialog = System.Windows.Forms.FolderBrowserDialog()
		if dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK:
			self._txtb_ext_tab_path.Text = dialog.SelectedPath

	def Btn_icon_pathClick(self, sender, e):
		dialog = System.Windows.Forms.OpenFileDialog()
		dialog.Filter = "PNG files (*.png)|*.png|All files (*.*)|*.*"
		if dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK:
			self._txtb_icon_path.Text = dialog.FileName

	def Btn_cancelClick(self, sender, e):
		self.Close()
		pass

	def Btn_okClick(self, sender, e):
		self.extTabPath = self._txtb_ext_tab_path.Text

		panelName = self._txtb_panel_name.Text
		buttonName = self._txtb_btn_name.Text
		extTabPath = self._txtb_ext_tab_path.Text

		#create panel directory
		panelDir = os.path.join(extTabPath, f"{panelName}.panel")
		os.makedirs(panelDir, exist_ok=True)


		#create a button inside panel directory
		buttonDir = os.path.join(panelDir, f"{buttonName}.pushbutton")
		os.makedirs(buttonDir, exist_ok=True)

		#Update bundle.yaml 
		bundleFile = os.path.join(extTabPath, 'bundle.yaml')
		panelEntry = f" - {panelName}"

		if not os.path.exists(bundleFile):
			with open(bundleFile, 'w') as file:
				file.write(f"{panelEntry} \n")
		else:
			with open(bundleFile, 'r') as file:
				content = file.readlines()
			if panelEntry not in content:
				content.append(f"{panelEntry} \n")
			with open(bundleFile, 'w') as file:
				file.writelines(content)

		selectedType = self._cbbx_sel_file.SelectedItem
		sourceFilePath = self._txtb_file_path.Text  # Get the selected file path from the text box

		if selectedType == '.dy':
			pyFilePath = os.path.join(buttonDir, 'script.py')
			with open(pyFilePath, 'w') as pyFile:
				pyFile.write("print('Welcome to BIM3DM')")


				# Handle file operations based on selected file type
		selectedType = self._cbbSourceFile.SelectedItem
		sourceFilePath = self._txtbSourceFilePath.Text  # Get the selected file path from the text box

		if selectedType == '.py':
			pyFilePath = os.path.join(buttonDir, 'script.py')
			with open(pyFilePath, 'w') as pyFile:
				pyFile.write("print('Welcome to BIM3DM')")
		elif selectedType == '.dyn':
			if os.path.exists(sourceFilePath):
				destinationFilePath = os.path.join(buttonDir, os.path.basename(sourceFilePath))
				shutil.copy2(sourceFilePath, destinationFilePath)

				# Copy the original file and rename it to _script.dyn
				scriptFilePath = os.path.splitext(destinationFilePath)[0] + '_script.dyn'
				shutil.copy2(sourceFilePath, scriptFilePath)
		elif selectedType == '.dll':
			if os.path.exists(sourceFilePath):
				destinationFilePath = os.path.join(buttonDir, os.path.basename(sourceFilePath))
				shutil.copy2(sourceFilePath, destinationFilePath)

		# Copy the selected icon file into the pushbutton directory and rename it to icon.png
		iconFilePath = self._txtbIconPath.Text
		if os.path.exists(iconFilePath):
			iconDestPath = os.path.join(buttonDir, 'icon.png')
			shutil.copy2(iconFilePath, iconDestPath)

		self.Close()
		

		



		self.Close()

	def Cbbx_sel_fileSelectedIndexChanged(self, sender, e):
		selectedType = self._cbbx_sel_file.SelectedItem
		if selectedType == '.py':
			self._txtb_file_path.Text = ""
		elif selectedType in ['.dyn', '.dll']:
			dialog = System.Windows.Forms.OpenFileDialog()
			dialog.Filter = f"{selectedType} files (*{selectedType})|*{selectedType}| All files (*.*)|*.*"
			if dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK:
				self._txtb_file_path.Text = dialog.FileName


f = MainForm()
Application.Run(f)
OUT = f.pyFilePath
