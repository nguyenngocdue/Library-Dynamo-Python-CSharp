{
  "Uuid": "f8c7f085-d337-43ad-8668-f469cc6ca278",
  "IsCustomNode": false,
  "Description": null,
  "Name": "Test_Function.py",
  "ElementResolver": {
    "ResolutionMap": {}
  },
  "Inputs": [],
  "Outputs": [],
  "Nodes": [
    {
      "ConcreteType": "Dynamo.Nodes.DSModelElementsSelection, DSRevitNodesUI",
      "NodeType": "ExtensionNode",
      "InstanceId": [
        "7dd12c62-c398-4b7a-ba88-51af503e59c6-0389132e",
        "a0b2b2cf-c416-4148-a62d-2892f36ecfd2-03891eaf",
        "a0b2b2cf-c416-4148-a62d-2892f36ecfd2-03891f8c"
      ],
      "Id": "d8bd260b14fd4199a766e804bf271983",
      "Inputs": [],
      "Outputs": [
        {
          "Id": "eed2fa487ba347418fa124cc9e46071d",
          "Name": "Elements",
          "Description": "The selected elements.",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled"
    },
    {
      "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
      "NodeType": "PythonScriptNode",
      "Code": "\"\"\"Copyright(c) 2019 by: duengocnguyen@gmail.com\"\"\"\r\n'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'\r\n\"\"\"________________Welcome to BIM3DM-DYNAMO API___________________\"\"\"\r\nimport clr \r\nimport sys\r\nsys.path.append(r'C:\\Program Files\\Autodesk\\Revit 2020\\AddIns\\DynamoForRevit\\IronPython.StdLib.2.7.8')\r\nimport math \r\nfrom System.Collections.Generic import *\r\n\r\nclr.AddReference(\"ProtoGeometry\")\r\nfrom Autodesk.DesignScript.Geometry import *\r\n\r\nclr.AddReference('RevitAPI')\r\nimport Autodesk\r\nfrom Autodesk.Revit.DB import *\r\n\r\nclr.AddReference('RevitAPIUI')\r\nfrom Autodesk.Revit.UI import*\r\nfrom  Autodesk.Revit.UI.Selection import*\r\n\r\nclr.AddReference(\"RevitNodes\")\r\nimport Revit\r\nclr.ImportExtensions(Revit.Elements)\r\nclr.ImportExtensions(Revit.GeometryConversion)\r\n\r\nclr.AddReference(\"RevitServices\")\r\nimport RevitServices\r\nfrom RevitServices.Persistence import DocumentManager\r\nfrom RevitServices.Transactions import TransactionManager\r\n\r\ndef get_geometry(element, include_invisible=False):\r\n    geom_opts = DB.Options()\r\n    geom_opts.IncludeNonVisibleObjects = include_invisible\r\n    geom_objs = []\r\n    for gobj in element.Geometry[geom_opts]:\r\n        if isinstance(gobj, DB.GeometryInstance):\r\n            inst_geom = gobj.GetInstanceGeometry()\r\n            geom_objs.extend(list(inst_geom))\r\n        else:\r\n            geom_objs.append(gobj)\r\n    return geom_objs\r\n    \r\ndoc = DocumentManager.Instance.CurrentDBDocument\r\nview = doc.ActiveView\r\nuidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument\r\nDB = Autodesk.Revit.DB\r\n\r\nelement = UnwrapElement(IN[0])\r\n\r\n\r\n\r\nOUT = [get_geometry( i) for i in element]",
      "Engine": "IronPython2",
      "VariableInputPorts": true,
      "Id": "77f8526d690a43109fcc75d178993503",
      "Inputs": [
        {
          "Id": "627a13b084614bee8de69ddf59a4a2bd",
          "Name": "IN[0]",
          "Description": "Input #0",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Outputs": [
        {
          "Id": "5f1551fe0be6477892be924eae40f8bb",
          "Name": "OUT",
          "Description": "Result of the python script",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled",
      "Description": "Runs an embedded Python script."
    },
    {
      "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
      "NodeType": "PythonScriptNode",
      "Code": "\"\"\"Copyright(c) 2019 by: duengocnguyen@gmail.com\"\"\"\r\n'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'\r\n\"\"\"________________Welcome to BIM3DM-DYNAMO API___________________\"\"\"\r\nimport clr \r\nimport sys\r\nsys.path.append(r'C:\\Program Files\\Autodesk\\Revit 2020\\AddIns\\DynamoForRevit\\IronPython.StdLib.2.7.8')\r\nimport math \r\nfrom System.Collections.Generic import *\r\n\r\nclr.AddReference(\"ProtoGeometry\")\r\nfrom Autodesk.DesignScript.Geometry import *\r\n\r\nclr.AddReference('RevitAPI')\r\nimport Autodesk\r\nfrom Autodesk.Revit.DB import *\r\n\r\nclr.AddReference('RevitAPIUI')\r\nfrom Autodesk.Revit.UI import*\r\nfrom  Autodesk.Revit.UI.Selection import*\r\n\r\nclr.AddReference(\"RevitNodes\")\r\nimport Revit\r\nclr.ImportExtensions(Revit.Elements)\r\nclr.ImportExtensions(Revit.GeometryConversion)\r\n\r\nclr.AddReference(\"RevitServices\")\r\nimport RevitServices\r\nfrom RevitServices.Persistence import DocumentManager\r\nfrom RevitServices.Transactions import TransactionManager\r\n\r\ndoc = DocumentManager.Instance.CurrentDBDocument\r\nview = doc.ActiveView\r\nuidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument\r\n\r\n#Preparing input from dynamo to revit\r\nelement = UnwrapElement(IN[0])\r\n\r\n#Do some action in a Transaction\r\n#TransactionManager.Instance.EnsureInTransaction(doc)\r\n\"\"\"Now, You Can Code \"\"\"\r\n\r\n\r\n\r\n#TransactionManager.Instance.TransactionTaskDone()\r\n\r\nOUT = [i.Name for i in  element]",
      "Engine": "IronPython2",
      "VariableInputPorts": true,
      "Id": "04b8a7d80c3047b7876c15bfd25bc352",
      "Inputs": [
        {
          "Id": "12075b95b3334c399d122704de2b974d",
          "Name": "IN[0]",
          "Description": "Input #0",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Outputs": [
        {
          "Id": "b9ebafa0b2a34d2e91c1b5d7196e0223",
          "Name": "OUT",
          "Description": "Result of the python script",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled",
      "Description": "Runs an embedded Python script."
    },
    {
      "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
      "NodeType": "PythonScriptNode",
      "Code": "\"\"\"Copyright(c) 2019 by: duengocnguyen@gmail.com\"\"\"\r\n'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'\r\n\"\"\"________________Welcome to BIM3DM-DYNAMO API___________________\"\"\"\r\nimport clr \r\nimport sys\r\nsys.path.append(r'C:\\Program Files\\Autodesk\\Revit 2020\\AddIns\\DynamoForRevit\\IronPython.StdLib.2.7.8')\r\nimport math \r\nfrom System.Collections.Generic import *\r\n\r\nclr.AddReference(\"ProtoGeometry\")\r\nfrom Autodesk.DesignScript.Geometry import *\r\n\r\nclr.AddReference('RevitAPI')\r\nimport Autodesk\r\nfrom Autodesk.Revit.DB import *\r\n\r\nclr.AddReference('RevitAPIUI')\r\nfrom Autodesk.Revit.UI import*\r\nfrom  Autodesk.Revit.UI.Selection import*\r\n\r\nclr.AddReference(\"RevitNodes\")\r\nimport Revit\r\nclr.ImportExtensions(Revit.Elements)\r\nclr.ImportExtensions(Revit.GeometryConversion)\r\n\r\nclr.AddReference(\"RevitServices\")\r\nimport RevitServices\r\nfrom RevitServices.Persistence import DocumentManager\r\nfrom RevitServices.Transactions import TransactionManager\r\n\r\ndoc = DocumentManager.Instance.CurrentDBDocument\r\nview = doc.ActiveView\r\nuidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument\r\n\r\n#Preparing input from dynamo to revit\r\nelement = UnwrapElement(IN[0])\r\n\r\n#Do some action in a Transaction\r\n#TransactionManager.Instance.EnsureInTransaction(doc)\r\n\"\"\"Now, You Can Code \"\"\"\r\n\r\n\r\n\r\n#TransactionManager.Instance.TransactionTaskDone()\r\n\r\nOUT = [j.ToProtoType() for i in element for j in i  ]",
      "Engine": "IronPython2",
      "VariableInputPorts": true,
      "Id": "c9f825117f7e4eb79110531e6a8c0bcb",
      "Inputs": [
        {
          "Id": "2312b49653ce41be9bd72247f2b796b3",
          "Name": "IN[0]",
          "Description": "Input #0",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Outputs": [
        {
          "Id": "522205efb15741baa3b2a8df8b7c96b9",
          "Name": "OUT",
          "Description": "Result of the python script",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled",
      "Description": "Runs an embedded Python script."
    },
    {
      "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
      "NodeType": "PythonScriptNode",
      "Code": "\"\"\"Copyright(c) 2019 by: duengocnguyen@gmail.com\"\"\"\r\n'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'\r\n\"\"\"________________Welcome to BIM3DM-DYNAMO API___________________\"\"\"\r\nimport clr \r\nimport sys\r\nsys.path.append(r'C:\\Program Files\\Autodesk\\Revit 2020\\AddIns\\DynamoForRevit\\IronPython.StdLib.2.7.8')\r\nimport math \r\nfrom System.Collections.Generic import *\r\n\r\nclr.AddReference(\"ProtoGeometry\")\r\nfrom Autodesk.DesignScript.Geometry import *\r\n\r\nclr.AddReference('RevitAPI')\r\nimport Autodesk\r\nfrom Autodesk.Revit.DB import *\r\n\r\nclr.AddReference('RevitAPIUI')\r\nfrom Autodesk.Revit.UI import*\r\nfrom  Autodesk.Revit.UI.Selection import*\r\n\r\nclr.AddReference(\"RevitNodes\")\r\nimport Revit\r\nclr.ImportExtensions(Revit.Elements)\r\nclr.ImportExtensions(Revit.GeometryConversion)\r\n\r\nclr.AddReference(\"RevitServices\")\r\nimport RevitServices\r\nfrom RevitServices.Persistence import DocumentManager\r\nfrom RevitServices.Transactions import TransactionManager\r\n\r\ndef get_sheets(include_placeholders=True, include_noappear=True, doc=None):\r\n    sheets = list(DB.FilteredElementCollector(doc or DOCS.doc)\r\n                  .OfCategory(DB.BuiltInCategory.OST_Sheets)\r\n                  .WhereElementIsNotElementType())\r\n    if not include_noappear:\r\n        sheets = [x for x in sheets\r\n                  if x.Parameter[DB.BuiltInParameter.SHEET_SCHEDULED]\r\n                  .AsInteger() > 0]\r\n    if not include_placeholders:\r\n        return [x for x in sheets if not x.IsPlaceholder]\r\n    return sheets\r\n     \r\n\r\ndoc = DocumentManager.Instance.CurrentDBDocument\r\nview = doc.ActiveView\r\nuidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument\r\nDB = Autodesk.Revit.DB\r\n\r\nelement = UnwrapElement(IN[0])\r\n\r\nOUT = get_sheets(True,True, doc)",
      "Engine": "IronPython2",
      "VariableInputPorts": true,
      "Id": "a101f50e7ea9437c97b9057a85aab944",
      "Inputs": [
        {
          "Id": "71e63d16f01340269502dc8fa57cf430",
          "Name": "IN[0]",
          "Description": "Input #0",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Outputs": [
        {
          "Id": "282bf3fe673248f6871d83efd82338b9",
          "Name": "OUT",
          "Description": "Result of the python script",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled",
      "Description": "Runs an embedded Python script."
    },
    {
      "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
      "NodeType": "PythonScriptNode",
      "Code": "\"\"\"Copyright(c) 2019 by: duengocnguyen@gmail.com\"\"\"\r\n'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'\r\n\"\"\"________________Welcome to BIM3DM-DYNAMO API___________________\"\"\"\r\nimport clr \r\nimport sys\r\nsys.path.append(r'C:\\Program Files\\Autodesk\\Revit 2020\\AddIns\\DynamoForRevit\\IronPython.StdLib.2.7.8')\r\nimport math \r\nfrom System.Collections.Generic import *\r\n\r\nclr.AddReference(\"ProtoGeometry\")\r\nfrom Autodesk.DesignScript.Geometry import *\r\n\r\nclr.AddReference('RevitAPI')\r\nimport Autodesk\r\nfrom Autodesk.Revit.DB import *\r\n\r\nclr.AddReference('RevitAPIUI')\r\nfrom Autodesk.Revit.UI import*\r\nfrom  Autodesk.Revit.UI.Selection import*\r\n\r\nclr.AddReference(\"RevitNodes\")\r\nimport Revit\r\nclr.ImportExtensions(Revit.Elements)\r\nclr.ImportExtensions(Revit.GeometryConversion)\r\n\r\nclr.AddReference(\"RevitServices\")\r\nimport RevitServices\r\nfrom RevitServices.Persistence import DocumentManager\r\nfrom RevitServices.Transactions import TransactionManager\r\n\r\ndef get_sheets(include_placeholders=True, include_noappear=True, doc=None):\r\n    sheets = list(DB.FilteredElementCollector(doc or DOCS.doc)\r\n                  .OfCategory(DB.BuiltInCategory.OST_Sheets)\r\n                  .WhereElementIsNotElementType())\r\n    if not include_noappear:\r\n        sheets = [x for x in sheets\r\n                  if x.Parameter[DB.BuiltInParameter.SHEET_SCHEDULED]\r\n                  .AsInteger() > 0]\r\n    if not include_placeholders:\r\n        return [x for x in sheets if not x.IsPlaceholder]\r\n    return sheets\r\n     \r\n\r\ndoc = DocumentManager.Instance.CurrentDBDocument\r\nview = doc.ActiveView\r\nuidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument\r\nDB = Autodesk.Revit.DB\r\n\r\nelement = UnwrapElement(IN[0])\r\n\r\nOUT = get_sheets(True,True, doc)",
      "Engine": "IronPython2",
      "VariableInputPorts": true,
      "Id": "fe5f859416e6479ea6ec22663b61dbc3",
      "Inputs": [
        {
          "Id": "03cfb6ef0f61421f9d76e01697b8e643",
          "Name": "IN[0]",
          "Description": "Input #0",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Outputs": [
        {
          "Id": "1e75d1edcf43463c9b5a6b647ed369a4",
          "Name": "OUT",
          "Description": "Result of the python script",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled",
      "Description": "Runs an embedded Python script."
    },
    {
      "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
      "NodeType": "PythonScriptNode",
      "Code": "\"\"\"Copyright(c) 2019 by: duengocnguyen@gmail.com\"\"\"\r\n'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'\r\n\"\"\"________________Welcome to BIM3DM-DYNAMO API___________________\"\"\"\r\nimport clr \r\nimport sys\r\nsys.path.append(r'C:\\Program Files\\Autodesk\\Revit 2020\\AddIns\\DynamoForRevit\\IronPython.StdLib.2.7.8')\r\nimport math \r\nfrom System.Collections.Generic import *\r\n\r\nclr.AddReference(\"ProtoGeometry\")\r\nfrom Autodesk.DesignScript.Geometry import *\r\n\r\nclr.AddReference('RevitAPI')\r\nimport Autodesk\r\nfrom Autodesk.Revit.DB import *\r\n\r\nclr.AddReference('RevitAPIUI')\r\nfrom Autodesk.Revit.UI import*\r\nfrom  Autodesk.Revit.UI.Selection import*\r\n\r\nclr.AddReference(\"RevitNodes\")\r\nimport Revit\r\nclr.ImportExtensions(Revit.Elements)\r\nclr.ImportExtensions(Revit.GeometryConversion)\r\n\r\nclr.AddReference(\"RevitServices\")\r\nimport RevitServices\r\nfrom RevitServices.Persistence import DocumentManager\r\nfrom RevitServices.Transactions import TransactionManager\r\n\r\nDB = Autodesk.Revit.DB\r\nGRAPHICAL_VIEWTYPES = [\r\n    DB.ViewType.FloorPlan,\r\n    DB.ViewType.CeilingPlan,\r\n    DB.ViewType.Elevation,\r\n    DB.ViewType.ThreeD,\r\n    DB.ViewType.Schedule,\r\n    DB.ViewType.DrawingSheet,\r\n    DB.ViewType.Report,\r\n    DB.ViewType.DraftingView,\r\n    DB.ViewType.Legend,\r\n    DB.ViewType.EngineeringPlan,\r\n    DB.ViewType.AreaPlan,\r\n    DB.ViewType.Section,\r\n    DB.ViewType.Detail,\r\n    DB.ViewType.CostReport,\r\n    DB.ViewType.LoadsReport,\r\n    DB.ViewType.PresureLossReport,\r\n    DB.ViewType.ColumnSchedule,\r\n    DB.ViewType.PanelSchedule,\r\n    DB.ViewType.Walkthrough,\r\n    DB.ViewType.Rendering\r\n]\r\ndef get_all_views(doc=None, view_types=None, include_nongraphical=False):\r\n    doc = doc or DOCS.doc\r\n    all_views = DB.FilteredElementCollector(doc) \\\r\n                  .OfClass(DB.View) \\\r\n                  .WhereElementIsNotElementType() \\\r\n                  .ToElements()\r\n\r\n    if view_types:\r\n        all_views = [x for x in all_views if x.ViewType in view_types]\r\n\r\n    if not include_nongraphical:\r\n        return [x for x in all_views\r\n                if x.ViewType in GRAPHICAL_VIEWTYPES\r\n                and not x.IsTemplate\r\n                and not x.ViewSpecific]\r\n\r\n    return all_views\r\n\r\ndoc = DocumentManager.Instance.CurrentDBDocument\r\nview = doc.ActiveView\r\nuidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument\r\n\r\n\r\nelement = IN[0]\r\n\r\nOUT = get_all_views(doc)\r\n",
      "Engine": "IronPython2",
      "VariableInputPorts": true,
      "Id": "510f6eea81ee43098bc76753414d4404",
      "Inputs": [
        {
          "Id": "24d75ad0242f4ed593bc5daf9964744c",
          "Name": "IN[0]",
          "Description": "Input #0",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Outputs": [
        {
          "Id": "2e19528dc059492eb9bcec7a2bbb5cc7",
          "Name": "OUT",
          "Description": "Result of the python script",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled",
      "Description": "Runs an embedded Python script."
    },
    {
      "ConcreteType": "PythonNodeModels.PythonNode, PythonNodeModels",
      "NodeType": "PythonScriptNode",
      "Code": "\"\"\"Copyright(c) 2019 by: duengocnguyen@gmail.com\"\"\"\r\n'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'\r\n\"\"\"________________Welcome to BIM3DM-DYNAMO API___________________\"\"\"\r\nimport clr \r\nimport sys\r\nsys.path.append(r'C:\\Program Files\\Autodesk\\Revit 2020\\AddIns\\DynamoForRevit\\IronPython.StdLib.2.7.8')\r\nimport math \r\nfrom System.Collections.Generic import *\r\n\r\nclr.AddReference(\"ProtoGeometry\")\r\nfrom Autodesk.DesignScript.Geometry import *\r\n\r\nclr.AddReference('RevitAPI')\r\nimport Autodesk\r\nfrom Autodesk.Revit.DB import *\r\n\r\nclr.AddReference('RevitAPIUI')\r\nfrom Autodesk.Revit.UI import*\r\nfrom  Autodesk.Revit.UI.Selection import*\r\n\r\nclr.AddReference(\"RevitNodes\")\r\nimport Revit\r\nclr.ImportExtensions(Revit.Elements)\r\nclr.ImportExtensions(Revit.GeometryConversion)\r\n\r\nclr.AddReference(\"RevitServices\")\r\nimport RevitServices\r\nfrom RevitServices.Persistence import DocumentManager\r\nfrom RevitServices.Transactions import TransactionManager\r\nDB = Autodesk.Revit.DB\r\ndef get_all_elements_in_view(view):\r\n    return DB.FilteredElementCollector(view.Document, view.Id)\\\r\n             .WhereElementIsNotElementType()\\\r\n             .ToElements()\r\n    \r\ndoc = DocumentManager.Instance.CurrentDBDocument\r\nview = doc.ActiveView\r\nuidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument\r\n\r\n\r\nelement = UnwrapElement(IN[0])\r\n\r\n\r\n\r\nOUT = get_all_elements_in_view(view)",
      "Engine": "IronPython2",
      "VariableInputPorts": true,
      "Id": "2788db0001c142f08bd22a75ebd98ea3",
      "Inputs": [
        {
          "Id": "72016ec021954f6d8fd642c5a98d2091",
          "Name": "IN[0]",
          "Description": "Input #0",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Outputs": [
        {
          "Id": "ea16505ce77f4d5aa2c48cbb089551ef",
          "Name": "OUT",
          "Description": "Result of the python script",
          "UsingDefaultValue": false,
          "Level": 2,
          "UseLevels": false,
          "KeepListStructure": false
        }
      ],
      "Replication": "Disabled",
      "Description": "Runs an embedded Python script."
    }
  ],
  "Connectors": [
    {
      "Start": "eed2fa487ba347418fa124cc9e46071d",
      "End": "627a13b084614bee8de69ddf59a4a2bd",
      "Id": "766d9372902a4da89685d4bb673e4f42"
    },
    {
      "Start": "5f1551fe0be6477892be924eae40f8bb",
      "End": "2312b49653ce41be9bd72247f2b796b3",
      "Id": "5d608a0f6d0b4520b91775b647234695"
    }
  ],
  "Dependencies": [],
  "NodeLibraryDependencies": [],
  "Bindings": [],
  "View": {
    "Dynamo": {
      "ScaleFactor": 1.0,
      "HasRunWithoutCrash": true,
      "IsVisibleInDynamoLibrary": true,
      "Version": "2.10.1.3976",
      "RunType": "Automatic",
      "RunPeriod": "1000"
    },
    "Camera": {
      "Name": "Background Preview",
      "EyeX": 247.33749389648438,
      "EyeY": 306.21072387695313,
      "EyeZ": 414.73870849609375,
      "LookX": -247.33749389648438,
      "LookY": -306.21072387695313,
      "LookZ": -414.73870849609375,
      "UpX": -0.17518346011638641,
      "UpY": 0.93969261646270752,
      "UpZ": -0.29374933242797852
    },
    "NodeViews": [
      {
        "ShowGeometry": true,
        "Name": "Select Model Elements",
        "Id": "d8bd260b14fd4199a766e804bf271983",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": true,
        "X": 2160.2883046775423,
        "Y": 377.65129903364306
      },
      {
        "ShowGeometry": true,
        "Name": "Python Script",
        "Id": "77f8526d690a43109fcc75d178993503",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": false,
        "X": 2528.9294867794983,
        "Y": 403.18953167488229
      },
      {
        "ShowGeometry": true,
        "Name": "Python Script",
        "Id": "04b8a7d80c3047b7876c15bfd25bc352",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": true,
        "X": 2138.7655690641077,
        "Y": 226.73132394167604
      },
      {
        "ShowGeometry": true,
        "Name": "Python Script",
        "Id": "c9f825117f7e4eb79110531e6a8c0bcb",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": false,
        "X": 2742.919943233001,
        "Y": 403.12792266446064
      },
      {
        "ShowGeometry": true,
        "Name": "Python Script",
        "Id": "a101f50e7ea9437c97b9057a85aab944",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": true,
        "X": 2621.9760997862572,
        "Y": 661.41964040891207
      },
      {
        "ShowGeometry": true,
        "Name": "Python Script",
        "Id": "fe5f859416e6479ea6ec22663b61dbc3",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": true,
        "X": 2989.9918205813092,
        "Y": 611.909599206662
      },
      {
        "ShowGeometry": true,
        "Name": "Python Script",
        "Id": "510f6eea81ee43098bc76753414d4404",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": true,
        "X": 7090.3128347267584,
        "Y": 1085.75051775145
      },
      {
        "ShowGeometry": true,
        "Name": "Python Script",
        "Id": "2788db0001c142f08bd22a75ebd98ea3",
        "IsSetAsInput": false,
        "IsSetAsOutput": false,
        "Excluded": false,
        "X": 712.52624476782,
        "Y": 325.117465280886
      }
    ],
    "Annotations": [],
    "X": -249.25697123378382,
    "Y": -477.788840365993,
    "Zoom": 1.7309445118284568
  }
}