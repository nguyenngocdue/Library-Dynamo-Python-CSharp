#filtering all family instances
collector = FilteredElementCollector(doc, view.Id)
familyFramingElements = collector.OfCategory(BuiltInCategory.OST_StructuralFraming).WhereElementIsNotElementType().ToElements()
familyFramingNames = { element.Name : element for element in familyFramingElements}
print(familyFramingNames)