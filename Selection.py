#public
def classifyElementsByCategory(uidoc, selection_filter, prompt):
    filters = SelectionFilter(*selection_filter)
    elSelectAll = uidoc.Selection.PickElementsByRectangle(filters, prompt)
    # Use a dictionary to store elements grouped by category
    categorized_elements = {}
    for element in elSelectAll:
        category_name = element.Category.Name
        if category_name not in categorized_elements:
            categorized_elements[category_name] = []
        categorized_elements[category_name].append(element)
    return categorized_elements

def isolateElement(self,elements):
    TransactionManager.Instance.EnsureInTransaction(doc)
    reset = View.DisableTemporaryViewMode(TemporaryViewMode.TemporaryHideIsolate)
    IDS = List[ElementId]()
    for i in elements:
        IDS.Add(i.Id)
    View.IsolateElementsTemporary(IDS)
    TransactionManager.Instance.TransactionTaskDone()