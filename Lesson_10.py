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
from  Autodesk.Revit.UI.Selection import*
from  Autodesk.Revit.UI.Selection import ISelectionFilter

import os
import shutil

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
#########################################################################
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *

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


	

################################################################

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btnSelectEle = System.Windows.Forms.Button()
		self._chlbxEle = System.Windows.Forms.CheckedListBox()
		self._lstbxEle = System.Windows.Forms.ListBox()
		self._lstviewEle = System.Windows.Forms.ListView()
		self._cbbxEle = System.Windows.Forms.ComboBox()
		self._txtbxTotalEle = System.Windows.Forms.TextBox()
		self._dataGridView1 = System.Windows.Forms.DataGridView()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._btnok = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		# self._dataGridView1.BeginInit()
		self.SuspendLayout()
		# 
		# btnSelectEle
		# 
		self._btnSelectEle.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btnSelectEle.Location = System.Drawing.Point(22, 24)
		self._btnSelectEle.Name = "btnSelectEle"
		self._btnSelectEle.Size = System.Drawing.Size(260, 46)
		self._btnSelectEle.TabIndex = 0
		self._btnSelectEle.Text = "Select"
		self._btnSelectEle.UseVisualStyleBackColor = True
		self._btnSelectEle.Click += self.BtnSelectEleClick
		# 
		# chlbxEle
		# 
		self._chlbxEle.FormattingEnabled = True
		self._chlbxEle.DisplayMember = "Name"
		self._chlbxEle.Location = System.Drawing.Point(22, 122)
		self._chlbxEle.Name = "chlbxEle"
		self._chlbxEle.Size = System.Drawing.Size(260, 169)
		self._chlbxEle.TabIndex = 1
		# 
		# lstbxEle
		# 
		self._lstbxEle.FormattingEnabled = True
		self._lstbxEle.DisplayMember = "Name"
		self._lstbxEle.Location = System.Drawing.Point(303, 122)
		self._lstbxEle.Name = "lstbxEle"
		self._lstbxEle.Size = System.Drawing.Size(231, 173)
		self._lstbxEle.TabIndex = 2
		# 
		# lstviewEle
		# 
		self._lstviewEle.Location = System.Drawing.Point(567, 122)
		self._lstviewEle.Name = "lstviewEle"
		self._lstviewEle.Size = System.Drawing.Size(186, 173)
		self._lstviewEle.TabIndex = 3
		self._lstviewEle.UseCompatibleStateImageBehavior = False
		# 
		# cbbxEle
		# 
		self._cbbxEle.FormattingEnabled = True
		self._cbbxEle.DisplayMember = 'Name'
		self._cbbxEle.Location = System.Drawing.Point(789, 122)
		self._cbbxEle.Name = "cbbxEle"
		self._cbbxEle.Size = System.Drawing.Size(186, 21)
		self._cbbxEle.TabIndex = 4
		# 
		# txtbxTotalEle
		# 
		self._txtbxTotalEle.Location = System.Drawing.Point(22, 325)
		self._txtbxTotalEle.Name = "txtbxTotalEle"
		self._txtbxTotalEle.Size = System.Drawing.Size(161, 20)
		self._txtbxTotalEle.TabIndex = 5
		# 
		# dataGridView1
		# 
		self._dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
		self._dataGridView1.Location = System.Drawing.Point(22, 380)
		self._dataGridView1.Name = "dataGridView1"
		self._dataGridView1.Size = System.Drawing.Size(742, 222)
		self._dataGridView1.TabIndex = 6
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Location = System.Drawing.Point(22, 96)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(130, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "CheckedListBox"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label2.Location = System.Drawing.Point(303, 96)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 7
		self._label2.Text = "ListBox"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label3.Location = System.Drawing.Point(567, 96)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "ListView"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label4.Location = System.Drawing.Point(789, 96)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Combobox"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label5.Location = System.Drawing.Point(22, 299)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Textbox"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label6.Location = System.Drawing.Point(22, 354)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(141, 23)
		self._label6.TabIndex = 7
		self._label6.Text = "DataGridView"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# btnok
		# 
		self._btnok.Location = System.Drawing.Point(804, 559)
		self._btnok.Name = "btnok"
		self._btnok.Size = System.Drawing.Size(75, 23)
		self._btnok.TabIndex = 8
		self._btnok.Text = "OK"
		self._btnok.UseVisualStyleBackColor = True
		self._btnok.Click += self.BtnokClick
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(900, 559)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(75, 23)
		self._btnCancel.TabIndex = 8
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = True
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(1012, 614)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnok)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._dataGridView1)
		self.Controls.Add(self._txtbxTotalEle)
		self.Controls.Add(self._cbbxEle)
		self.Controls.Add(self._lstviewEle)
		self.Controls.Add(self._lstbxEle)
		self.Controls.Add(self._chlbxEle)
		self.Controls.Add(self._btnSelectEle)
		self.TopMost = True
		self.Name = "MainForm"
		self.Text = "Selection"

		# self._dataGridView1.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()



	def BtnSelectEleClick(self, sender, e):
		refs = uidoc.Selection.PickObjects(ObjectType.Element, "Select Elements")
		refs = getList(refs)
		elements = []
		for ref in refs:
			element = doc.GetElement(ref.ElementId)
			elements.append(element)
		self.elements = elements
		#checkedlistbox
		self._chlbxEle.Items.Clear()
		for item in elements:
			self._chlbxEle.Items.Add(item)
		#textbox
		self._txtbxTotalEle.Text = str(len(elements))

		#combobox
		self._cbbxEle.Items.Clear()
		for item in elements:
			self._cbbxEle.Items.Add(item)
		
		#listbox
		self._lstbxEle.Items.Clear()
		for item in elements:
			self._lstbxEle.Items.Add(item)

		#listView
		self._lstviewEle.Items.Clear()
		for item in elements:
			lstViewItem = ListViewItem()
			lstViewItem.Text = item.Name
			lstViewItem.SubItems.Add(str(item.Id))
			self._lstviewEle.Items.Add(lstViewItem)

		self._dataGridView1.Rows.Clear()
		self._dataGridView1.Columns.Clear()

		self._dataGridView1.Columns.Add("Id", "Id")
		self._dataGridView1.Columns.Add("Name", "Name")
		self._dataGridView1.Columns.Add("Status", "Status")

		for item in elements:
			self._dataGridView1.Rows.Add(item.Id, item.Name, "Ok")




	def BtnokClick(self, sender, e):
		self.Close()

	def BtnCancelClick(self, sender, e):
		self.Close()


f = MainForm()
Application.Run(f)
OUT = f.elements