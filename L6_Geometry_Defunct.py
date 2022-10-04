import clr
import System

from System.Collections.Generic import*

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import*

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import*

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)


clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

ele  = UnwrapElement(IN[1])

def GetSolidElement(element): # Get Geometry of Element
    geo = []
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.DetailLevel = ViewDetailLevel.Fine
    geometry = element.get_Geometry(opt)
    for i in geometry: geo.append(i) # Way 1
    #geo = [i for i in element.get_Geometry(opt)] # Way 2  
    return [i for i in geometry]

def GetSolidFromGeo(lstGeo): # Get Solid of Geometry 
    sol = []
    for i in lstGeo:
        if i.GetType() == Solid and i.Volume > 0:
            sol.append(i)
        elif i.GetType() == GeometryInstance:
            var = i.SymbolGeometry
            for j in var:
                if j.Volume > 0:
                    sol.append(j)
    return sol


def GetPlanarFormSolid(solids): # Get Faces from Solid
    faces = [] 
    for i in solids:
        faces.append(i.Faces)
    return faces[0]

def Isparallel(p,q):
    return p.CrossProduct(q).IsZeroLength() # U.V = 0 it is CrossProduct between  2 Vectors

def GetPlanarVertical(listPlanr): # Get Faces follow Vertical 
    reV = []
    y = XYZ.BasisY
    for i in listPlanr:
        var = i.FaceNormal
        check = Isparallel(var, y)
        # if check == True:
        #      reV.append(i)
        reV.append(i)
    return reV

def GetRefFromPlanar(listPlanr):
    re = []
    for i in listPlanr:
        re.append(i.Reference)
    return re


# def GetPlanrHorizontal(listPlanr): # Get Faces follow Horizontal
#     reH = []
#     z = XYZ.BasisZ
#     for i in listPlanr:
#         var = i.FaceNormal
#         check = Isparallel(z, var)
#         if check == True:
#             reH.append(i)
#         return reH



geo = GetSolidElement(ele)  # Get Geometry of Element
soli = GetSolidFromGeo(geo) # Get Solid of Geometry 
planr = GetPlanarFormSolid(soli) # Get Faces from Solid
vPlanr = GetPlanarVertical(planr)
ref = GetRefFromPlanar(vPlanr) # Get References from Vertical Planars


#OUT =geo ,soli , planr, verti, hori
OUT = vPlanr, ref