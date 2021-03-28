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

ele = UnwrapElement(IN[1])

def GetGeoElemnt(element): # Get Geometry of Element
    geo = []
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.DetailLevel = ViewDetailLevel.Fine
    geometry = element.get_Geometry(opt)
    geo = [i for i in geometry]
    return geo

def GetSolidFromGeo(lstgeometry): # Get Solid from Geometry
    sol = []
    for i in lstgeometry:
        if i.GetType()== Solid and i.Volume != 0:
            sol.append(i)
        elif i.GetType() == GeometryInstance:
            var = i.SymbolGeometry
            for j in var:
                if j.Volume != 0:
                    sol.append(j)
    return sol
        
def GetPlanarFromSolid(lstsolids): # Get PlanarFace from Solid
    pfaces = []
    for i in lstsolids:
        pfaces.append(i.Faces)
    return pfaces[0]

def Isparalel(p,q):
    return p.CrossProduct(q).IsZeroLength() # Tich co huong 2 Vector

def RemoveFaceNone(lstplanars): # Get planarFaces Not Null Value
    pfaces = []
    for i in lstplanars:
        if i.Reference != None:
            pfaces.append(i)
    return pfaces
 

def FilterVerticalPlanar(lstplanars): # Get plannar follow Vertical
    faV = []
    Y = XYZ.BasisY
    for i in RemoveFaceNone(lstplanars):
        var = i.FaceNormal
        check = Isparalel(Y,var)
        if check == True:
            faV.append(i)
    return faV

def FilterHorizontalPlanar(lstplans): # Get plannar follow Horizantal
    faH = []
    Z = XYZ.BasisZ
    for i in lstplans:
        var = i.FaceNormal
        check = Isparalel(Z,var)
        if check == True:
            faH.append(i)
    return faH

def RefFromPlanar(listPlanr): # Get References of Plannars
    re = []
    for i in listPlanr:
        if i.Reference != None:
            re.append(i.Reference)   
    return re


geoEle = GetGeoElemnt(ele)   # Get Geometry of Element
soli = GetSolidFromGeo(geoEle)    # Get Solid from Geometry
planar = GetPlanarFromSolid(soli)  # Get PlanarFace from Solid
faceVeti = FilterVerticalPlanar(planar)   # Get plannarFaces follow Vertical
faceHori = FilterHorizontalPlanar(planar)  # Get plannarFaces follow Horizantal
reV = RefFromPlanar(faceVeti)  # Get References of Plannars --> Vertical
reH = RefFromPlanar(faceHori)  # Get References of Plannars ---> Horizontal

OUT = reV, reH