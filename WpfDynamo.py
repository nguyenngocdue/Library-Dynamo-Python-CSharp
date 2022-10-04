import clr

clr.AddReference('PresentationFramework')
clr.AddReference('PresentationCore')

from System.Windows import Window
from System.Windows.Controls import StackPanel

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import PreviewControl

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

win = Window()
st = StackPanel()
st.Children.Add(PreviewControl(doc, doc.ActiveView.Id))

win.Content = st
win.Show()  