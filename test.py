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


#########################################################################

from System.Windows.Forms import Application, Form, ComboBox, ListView, View, ListViewItem

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()

    def InitializeComponent(self):
        self._listView1 = ListView()
        self._cbbx = ComboBox()
        self._btnOK = Button()
        self._btnCancel = Button()
        self.SuspendLayout()

        # listView1
        self._listView1.Location = System.Drawing.Point(12, 71)
        self._listView1.Name = "listView1"
        self._listView1.Size = System.Drawing.Size(250, 178)
        self._listView1.View = View.Details
        self._listView1.Columns.Add("Value")

        # cbbx
        self._cbbx.FormattingEnabled = True
        self._cbbx.Location = System.Drawing.Point(12, 27)
        self._cbbx.Name = "cbbx"
        self._cbbx.Size = System.Drawing.Size(250, 21)
        self._cbbx.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        self._cbbx.Items.AddRange(System.Array[System.Object](["a", "b", "c", "d"]))

        # btnOK
        self._btnOK.Location = System.Drawing.Point(12, 255)
        self._btnOK.Name = "btnOK"
        self._btnOK.Size = System.Drawing.Size(120, 30)
        self._btnOK.Text = "OK"
        self._btnOK.Click += self.BtnOKClick

        # btnCancel
        self._btnCancel.Location = System.Drawing.Point(142, 255)
        self._btnCancel.Name = "btnCancel"
        self._btnCancel.Size = System.Drawing.Size(120, 30)
        self._btnCancel.Text = "Cancel"
        self._btnCancel.Click += self.BtnCancelClick

        # MainForm
        self.ClientSize = System.Drawing.Size(284, 300)
        self.Controls.Add(self._cbbx)
        self.Controls.Add(self._listView1)
        self.Controls.Add(self._btnOK)
        self.Controls.Add(self._btnCancel)
        self.Name = "MainForm"
        self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        self.Text = "BIM3DM"
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

    def BtnOKClick(self, sender, e):
        # Add logic for OK button click
        print("OK button clicked")

    def BtnCancelClick(self, sender, e):
        # Add logic for Cancel button click
        print("Cancel button clicked")


Application.Run(MainForm())