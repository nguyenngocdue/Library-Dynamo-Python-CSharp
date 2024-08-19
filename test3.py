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
from  Autodesk.Revit.UI.Selection import*
from  Autodesk.Revit.UI.Selection import ISelectionFilter

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*
from Autodesk.Revit.DB import Line, ModelLine, LinePattern, ElementId
import Autodesk.Revit.DB as RDB
from Autodesk.Revit.DB import Line, GeometryInstance, Solid

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *

doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.load_values()
        self._comboBox1.SelectedIndexChanged += self.comboBox1_SelectedIndexChanged
        self._comboBox2.SelectedIndexChanged += self.comboBox2_SelectedIndexChanged
        self._comboBox3.SelectedIndexChanged += self.comboBox3_SelectedIndexChanged
        self._textBox1.TextChanged += self.calculate_sum
        self._textBox2.TextChanged += self.calculate_sum
        self._textBox3.TextChanged += self.calculate_sum
        self._buttonOK.Click += self.buttonOK_Click

    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._comboBox2 = System.Windows.Forms.ComboBox()
        self._label3 = System.Windows.Forms.Label()
        self._comboBox3 = System.Windows.Forms.ComboBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._buttonOK = System.Windows.Forms.Button()
        self.SuspendLayout()
        #
        # label1
        #
        self._label1.Location = System.Drawing.Point(30, 29)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Select Element A:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # label2
        #
        self._label2.Location = System.Drawing.Point(30, 79)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 0
        self._label2.Text = "Select Element B:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # comboBox1
        #
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Location = System.Drawing.Point(137, 30)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(318, 21)
        self._comboBox1.TabIndex = 1
        #
        # comboBox2
        #
        self._comboBox2.FormattingEnabled = True
        self._comboBox2.Location = System.Drawing.Point(137, 79)
        self._comboBox2.Name = "comboBox2"
        self._comboBox2.Size = System.Drawing.Size(318, 21)
        self._comboBox2.TabIndex = 1
        #
        # label3
        #
        self._label3.Location = System.Drawing.Point(30, 126)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 0
        self._label3.Text = "Select Element C:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # comboBox3
        #
        self._comboBox3.FormattingEnabled = True
        self._comboBox3.Location = System.Drawing.Point(136, 126)
        self._comboBox3.Name = "comboBox3"
        self._comboBox3.Size = System.Drawing.Size(318, 21)
        self._comboBox3.TabIndex = 1
        #
        # textBox1
        #
        self._textBox1.Location = System.Drawing.Point(88, 190)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 2
        #
        # label4
        #
        self._label4.Location = System.Drawing.Point(30, 190)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 0
        self._label4.Text = "Value X:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # label5
        #
        self._label5.Location = System.Drawing.Point(30, 213)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 0
        self._label5.Text = "Value B:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # textBox2
        #
        self._textBox2.Location = System.Drawing.Point(88, 213)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 2
        #
        # label6
        #
        self._label6.Location = System.Drawing.Point(30, 236)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 0
        self._label6.Text = "Value C:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # textBox3
        #
        self._textBox3.Location = System.Drawing.Point(88, 236)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 2
        #
        # label7
        #
        self._label7.Location = System.Drawing.Point(212, 213)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 0
        self._label7.Text = "A + B + C:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # textBox4
        #
        self._textBox4.Location = System.Drawing.Point(269, 215)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 20)
        self._textBox4.TabIndex = 2
        self._textBox4.ReadOnly = True
        #
        # buttonOK
        #
        self._buttonOK.Location = System.Drawing.Point(250, 300)
        self._buttonOK.Name = "buttonOK"
        self._buttonOK.Size = System.Drawing.Size(100, 30)
        self._buttonOK.TabIndex = 3
        self._buttonOK.Text = "OK"
        self._buttonOK.UseVisualStyleBackColor = True
        #
        # MainForm
        #
        self.ClientSize = System.Drawing.Size(617, 397)
        self.Controls.Add(self._buttonOK)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._comboBox3)
        self.Controls.Add(self._comboBox2)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        self.Text = "Form1"
        self.TopMost = True
        self.ResumeLayout(False)
        self.PerformLayout()

    def load_values(self):
        self.all_elements = [
            "Element1", "Element2", "Element3",
            "Element4", "Element5", "Element6",
            "Element7", "Element8", "Element9", "Element10"
        ]
        self._comboBox1.Items.AddRange(["Old", "Even", "All"])
        self._comboBox1.SelectedIndex = 0  # Select the first item by default
        self.update_comboboxes("odd")  # Initialize ComboBoxes B and C based on the first item

    def comboBox1_SelectedIndexChanged(self, sender, event):
        selected_value = self._comboBox1.SelectedItem
        if selected_value == "Old":
            self.update_comboboxes("odd")
        elif selected_value == "Even":
            self.update_comboboxes("even")
        elif selected_value == "All":
            self.update_comboboxes("all")
        

    def comboBox2_SelectedIndexChanged(self, sender, event):
        selected_value = self._comboBox2.SelectedItem
        self._textBox2.Text = str(self.get_value(selected_value))
        

    def comboBox3_SelectedIndexChanged(self, sender, event):
        selected_value = self._comboBox3.SelectedItem
        self._textBox3.Text = str(self.get_value(selected_value))
        

    def update_comboboxes(self, filter_type):
        self._comboBox2.Items.Clear()
        self._comboBox3.Items.Clear()

        if filter_type == "odd":
            odd_elements = [element for i, element in enumerate(self.all_elements) if i % 2 == 0]
            self._comboBox2.Items.AddRange(odd_elements)
            self._comboBox3.Items.AddRange([element for element in self.all_elements if element not in odd_elements])
        elif filter_type == "even":
            even_elements = [element for i, element in enumerate(self.all_elements) if i % 2 != 0]
            self._comboBox2.Items.AddRange(even_elements)
            self._comboBox3.Items.AddRange([element for element in self.all_elements if element not in even_elements])
        else:
            self._comboBox2.Items.AddRange(self.all_elements)
            self._comboBox3.Items.AddRange(self.all_elements)

        # Select the first item by default after updating
        if self._comboBox2.Items.Count > 0:
            self._comboBox2.SelectedIndex = 0
        if self._comboBox3.Items.Count > 0:
            self._comboBox3.SelectedIndex = 0

    def get_value(self, element):
        values = {
            "Element1": 10, "Element2": 20, "Element3": 30,
            "Element4": 40, "Element5": 50, "Element6": 60,
            "Element7": 70, "Element8": 80, "Element9": 90, "Element10": 100
        }
        return values.get(element, 0)

    def calculate_sum(self, sender, event):
        try:
            a = int(self._textBox1.Text)
        except ValueError:
            a = 0
        try:
            b = int(self._textBox2.Text)
        except ValueError:
            b = 0
        try:
            c = int(self._textBox3.Text)
        except ValueError:
            c = 0
        self._textBox4.Text = str(a + b + c)
        self.valueA = self._comboBox1.Text
        self.valueB = self._textBox2.Text
        self.valueC = self._textBox3.Text
        self.total = self._textBox4.Text

    def buttonOK_Click(self, sender, event):
        self.Close()

mainForm = MainForm()
Application.Run(mainForm)
OUT = mainForm.valueA, mainForm.valueB, mainForm.valueC, mainForm.total