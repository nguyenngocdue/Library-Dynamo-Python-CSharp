import os
import clr
clr.AddReference("System")   
import System
from System.ComponentModel import BackgroundWorker
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import*
from Autodesk.Revit.DB import Transaction, FilteredElementCollector
from System.Collections.Generic import List

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*


clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#-------------------------------------------------------------------
# WPF
try:
    clr.AddReference("IronPython.wpf")
    clr.AddReference('PresentationCore')
    clr.AddReference('PresentationFramework')
except IOError:
    raise
from System.IO import StringReader
from System.Windows.Markup import XamlReader, XamlWriter
from System.Windows import Window, Application, MessageBox, MessageBoxButton, MessageBoxResult
from System.Windows import RoutedEventHandler
from System.Runtime.InteropServices import Marshal
from System.Collections.ObjectModel import ObservableCollection
from System.Windows.Data import ListCollectionView
from System.ComponentModel import INotifyPropertyChanged
import clr
from System.Collections.ObjectModel import ObservableCollection
from System.Windows.Data import ListCollectionView
from System.ComponentModel import INotifyPropertyChanged, PropertyChangedEventArgs

try:
    import wpf
except ImportError:
    raise

#-------------------------------------------------------------------
def logger(title, content):
    import datetime
    date = datetime.datetime.now()
    f = open(r"A:\Library-Dynamo-Python-CSharp\python.log", 'a')
    f.write(str(date) + '\n' + title + '\n' + str(content) + '\n')
    f.close()

def getDataFromRows(rows_count, cols_count, start_row = 1, start_col = 1):
    data = []
    for row_index in range(start_row, rows_count + 1):
        colData = []
        for col_index in range(start_col, cols_count + 1):
            cell_value = str(workSheet.Cells[row_index, col_index].Value2)
            colData.append(cell_value)
        data.append(colData)
    return data


def getDataFromColumns(rows_count, cols_count, start_row=1, start_col=1):
    data = []
    for col_index in range(start_col, cols_count + 1):
        colData = []
        for row_index in range(start_row, rows_count + 1):
            cell_value = str(workSheet.Cells[row_index, col_index].Value2)
            colData.append(cell_value)
        data.append(colData)
    return data
#-------------------------------------------------------------------
doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
DB = Autodesk.Revit.DB

def getSheetTBlocks(src_sheet):
    sheet_tblocks = FilteredElementCollector(src_sheet.Document, src_sheet.Id) \
                    .OfCategory(BuiltInCategory.OST_TitleBlocks) \
                    .WhereElementIsNotElementType() \
                    .ToElements()
    if sheet_tblocks:
        title_block_name = sheet_tblocks[0].Name
        return title_block_name
    return None

def getAllTitleBlocks():
    titleBlockFilter = ElementCategoryFilter(BuiltInCategory.OST_TitleBlocks)
    collector = FilteredElementCollector(doc).WherePasses(titleBlockFilter).WhereElementIsNotElementType()
    titleBlockList = []
    for titleBlock in collector:
        titleBlockList.append(titleBlock)
    return titleBlockList

def createSheet(sheet_num, sheet_name,
                 titleBlock_id=DB.ElementId.InvalidElementId, doc=None):
    doc = DocumentManager.Instance.CurrentDBDocument
    TransactionManager.Instance.EnsureInTransaction(doc)
    newSheet = DB.ViewSheet.Create(doc, titleBlock_id)
    TransactionManager.Instance.TransactionTaskDone()
    newSheet.Name = sheet_name
    newSheet.SheetNumber = sheet_num
    return newSheet

def getAllSheets():
    collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType()
    sheetList = [] 
    for sheet in collector:
        sheetList.append(sheet)
    return sheetList

def getSheetInfoDictionary():
    collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType()
    sheetInfoDict = {}
    sheetNames = []
    sheetNumbers = []
    titleBlocks = []
    for sheet in collector:
        sheetNames.append(sheet.Name)
        sheetNumbers.append(sheet.SheetNumber)
        titleBlock = getSheetTBlocks(sheet)
        if not titleBlock: titleBlock = None
        titleBlocks.append(titleBlock)
        sheetInfoDict['sheet_names'] = sheetNames
        sheetInfoDict['sheet_numbers'] = sheetNumbers
        sheetInfoDict['title_blocks'] = titleBlocks
    return sheetInfoDict

#-------------------------------------------------------------------
# Read data from Excel into a 2D list
excel = Marshal.GetActiveObject("Excel.Application")
excel.Visible = True
excel.DisplayAlerts = False
filePath = r'A:\TRAINING DYNAMO API\PART 26 CURD Sheet\InforSheet.xlsx'
workbook = excel.Workbooks.Open(filePath)
workSheet = workbook.ActiveSheet

# Get the used range of the worksheet (including only the data)
usedRange = workSheet.UsedRange

# Get the number of rows and columns in the used range
rows_count = usedRange.Rows.Count
cols_count = usedRange.Columns.Count
start_row = 1
start_col = 2
# Read data from each row separately
dataOfRows = getDataFromRows(rows_count, cols_count, start_row, start_col)
dataOfCols = getDataFromColumns(rows_count, cols_count, start_row, start_col)

excel.Visible = True
Marshal.ReleaseComObject(excel)

keys = ['sheet_numbers','sheet_names', 'title_blocks']

dictInfoSheets = {k : i[1:] for i , k in zip(dataOfCols, keys)}
keysInfoSheets = dictInfoSheets.keys()
sheetNumbers = dictInfoSheets[keysInfoSheets[0]]
sheetNames =  dictInfoSheets[keysInfoSheets[2]]
titleBlocks = dictInfoSheets[keysInfoSheets[1]]
allTitleBlocks = getAllTitleBlocks()

sheetInfoDictionary = getSheetInfoDictionary()
sheetNumbersOnRevit = sheetInfoDictionary[keys[0]]

allSheets = getAllSheets()

# ----------------------------------------------------------------
#FORM
import clr
from System.Collections.ObjectModel import ObservableCollection
from System.Windows.Data import ListCollectionView
from System.ComponentModel import INotifyPropertyChanged, PropertyChangedEventArgs


class PropertyChangedEventHandler(object):
    def __init__(self, func):
        self.func = func

    def HandlePropertyChanged(self, sender, args):
        self.func(sender, args)

class ViewModelBase(INotifyPropertyChanged):
    PropertyChanged = None

    @staticmethod
    def add_PropertyChanged(instance, value):
        if instance.PropertyChanged is None:
            instance.PropertyChanged = PropertyChangedEventHandler(value).HandlePropertyChanged
        else:
            instance.PropertyChanged += PropertyChangedEventHandler(value).HandlePropertyChanged

    @staticmethod
    def remove_PropertyChanged(instance, value):
        if instance.PropertyChanged is not None:
            handler = PropertyChangedEventHandler(value).HandlePropertyChanged
            instance.PropertyChanged -= handler

    def OnPropertyChanged(self, prop_name=""):
        if self.PropertyChanged is not None:
            args = PropertyChangedEventArgs(prop_name)
            self.PropertyChanged(self, args)

class ViewModel():
    def __init__(self, cgv1, cgv2, cgv3, cgv4):
        self._gvNo = cgv1
        self._gvSheetNumber = cgv2
        self._gvSheetName = cgv3
        self._gvTitleBlock = cgv4

    @property
    def gvSheetName(self):
        return self._gvSheetName

    @property
    def gvSheetNumber(self):
        return self._gvSheetNumber

    @property
    def gvTitleBlock(self):
        return self._gvTitleBlock

    @property
    def gvNo(self):
        return self._gvNo

    @gvSheetName.setter
    def gvSheetName(self, value):
        if self._gvSheetName != value:
            self._gvSheetName = value
            self.OnPropertyChanged("gvSheetName")

    @gvSheetNumber.setter
    def gvSheetNumber(self, value):
        if self._gvSheetNumber != value:
            self._gvSheetNumber = value
            self.OnPropertyChanged("gvSheetNumber")

    @gvTitleBlock.setter
    def gvTitleBlock(self, value):
        if self._gvTitleBlock != value:
            self._gvTitleBlock = value
            self.OnPropertyChanged("gvTitleBlock")

    @gvNo.setter
    def gvNo(self, value):
        if self._gvNo != value:
            self._gvNo = value
            self.OnPropertyChanged("gvNo")

class MyWindow(Window):
    def __init__(self, dataModels):
        self.ui = wpf.LoadComponent(self, r'A:\TRAINING DYNAMO API\PART 26 CURD Sheet\Forms\CURD_SHEETS\CURD_SHEETS\MainWindow.xaml')
        self.selectedElements = []

        for k, v in dataModels.items():
            control = self.FindName(k)
            if control is not None:
                control.ItemsSource = v

    def OnItemPropertyChanged(self, sender, event):
        self.lvSheetsRevit.Items.Refresh()
        self.lvSheetsExcel.Items.Refresh()


    def btnRefresh(self, sender, event):
        MessageBox.Show('Loading data')
        self.loadExcelData()
    def loadExcelData(self):
        viewModelSheetsRevit = createModel(sheetInfoDictionary)
        viewModelSheetsExcel = createModel(dictInfoSheets)
        dataModels = {'lvSheetsRevit': viewModelSheetsRevit, 'lvSheetsExcel': viewModelSheetsExcel}
        self.lvSheetsRevit.ItemsSource = dataModels['lvSheetsRevit']
        self.lvSheetsExcel.ItemsSource = dataModels['lvSheetsExcel']
        self.refreshListView(self.lvSheetsExcel)
    def refreshListView(self, listView):
        collectionView = ListCollectionView(listView.ItemsSource)
        collectionView.Refresh()


    def btnUploadExcel(self, sender, event):
        pass

    def btnExploreExcel(self, sender, event):
        pass
    

    def btnCreateSheets(self, sender, event):
        sheets = []
        try:
            for i in range(len(dictInfoSheets['sheet_numbers'])):
                for num, name, titleBlock in zip(dictInfoSheets['sheet_numbers'], dictInfoSheets['sheet_names'], dictInfoSheets['title_blocks']):
                    if str(num) in sheetNumbersOnRevit:
                        for sheet in allSheets:
                            if sheet.SheetNumber ==  num and name != sheet.Name:
                                TransactionManager.Instance.EnsureInTransaction(doc)
                                sheet.Name = name
                                TransactionManager.Instance.TransactionTaskDone()
                    else:
                        sheet = createSheet(num, name)
                        sheets.append(sheet)
        except Exception as e:
            self.Hide()
            # After creating sheets, refresh the Revit UI to display the changes
            uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
            uidoc.RefreshActiveView()
            viewModelSheetsRevit = createModel(sheetInfoDictionary)
            for k, v in viewModelSheetsRevit.items():
                control = self.FindName(k)
                if control is not None:
                    control.ItemsSource = v
            # self.lvSheetsRevit.Items.Refresh()
            self.UpdateLayout()
            # self.Show()

    def btnCancel(self, sender, event):
        self.Close()


def createModel(dictData):
    # viewModelType = clr.GetClrType(ViewModel)
    # viewModels = ObservableCollection[viewModelType]()
    viewModels = []
    keys = dictData.keys()
    for i in range(len(dictData[keys[0]])):
        viewModel = ViewModel(
            cgv1=i + 1,
            cgv2=dictData[keys[0]][i],
            cgv3=dictData[keys[2]][i],
            cgv4=dictData[keys[1]][i],
        )
        viewModels.Add(viewModel)
    return viewModels

viewModelSheetsRevit = createModel(sheetInfoDictionary)
viewModelSheetsExcel = createModel(dictInfoSheets)
dataModels = {'lvSheetsRevit': viewModelSheetsRevit, 'lvSheetsExcel': viewModelSheetsExcel}

OUT = allTitleBlocks,allTitleBlocks[0].Id

myWindow = MyWindow(dataModels)
myWindow.ShowDialog()



