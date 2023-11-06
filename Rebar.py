def createRebarStyle(isStandard):
    if isStandard:
        return Autodesk.Revit.DB.Structure.RebarStyle().Standard
    return Autodesk.Revit.DB.Structure.RebarStyle().StirrupTie

def createRebarHookOrientation(isLeft):
    from Autodesk.Revit.DB.Structure import*
    if isLeft:
        return RebarHookOrientation.Left
    return RebarHookOrientation.Right