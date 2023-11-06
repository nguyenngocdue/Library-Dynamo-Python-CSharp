def getRebarType(isStandard):
    if(isStandard):
        return Autodesk.Revit.DB.Structure.RebarStyle().Standard
    return Autodesk.Revit.DB.Structure.RebarStyle().StirrupTie
