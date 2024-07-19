def getDbGrids(elementGrids): # Get Revit.DB.Reference from Grids
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    dbGrids = []
    for i in UnwrapElement(elementGrids):
        f = (i.get_Geometry(opt))
        for j in f:
            if j.GetType() == Line:
                dbGrids.append(j)
    return dbGrids
def getRefArrayFromGrids(grids,doc):
    refArray = ReferenceArray()
    opt = Options()
    opt.ComputeReferences= True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    for i in UnwrapElement(grids):
        f = (i.get_Geometry(opt))
        for j in f:
            if j.GetType() == Line:
                refArray.Append(j.Reference)
    return refArray