"""
Awesome code by Archiways found on Dynamo Forum https://forum.dynamobim.com/t/bounding-box-in-rotated-coordinate-system-rotated-bounding-box/50597
Expanded by Dan Woodcock for demonstration...
https://forum.dynamobim.com/t/rotate-transform-boundingbox/63435/3
"""

import clr

import sys 
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')

clr.AddReference('ProtoGeometry') 
import Autodesk.DesignScript.Geometry as DG
#from Autodesk.DesignScript.Geometry import * 

clr.AddReference("DSCoreNodes") 
import DSCore as DS
#from DSCore import *

clr.AddReference("RevitNodes") 
import Revit.Elements as DR
#from Revit.Elements import * 

import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion) 
#
clr.AddReference("RevitAPI") 
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Mechanical import *
from Autodesk.Revit.DB.Structure import *
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *

clr.AddReference("RevitServices") 
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
doc = DocumentManager.Instance.CurrentDBDocument

import System 
from System import Array as CArray
clr.AddReference("System") 
from System.Collections.Generic import List as CList


import math 

def RotatedBox(elements,angle):

	def SumBoxes(boxes):
		
		minx = min([b.Min.X for b in boxes])
		miny = min([b.Min.Y for b in boxes])
		minz = min([b.Min.Z for b in boxes])
		maxx = max([b.Max.X for b in boxes])
		maxy = max([b.Max.Y for b in boxes])
		maxz = max([b.Max.Z for b in boxes])
		
		bb = BoundingBoxXYZ()
		bb.Min = XYZ(minx,miny,minz)
		bb.Max = XYZ(maxx,maxy,maxz)
		return bb


	def GeoBox(g):
	
		box = g.GetBoundingBox()
		origin = box.Transform.Origin
		box.Min = box.Min.Add(origin)
		box.Max = box.Max.Add(origin)
		return box


	if hasattr(elements, '__iter__') == False:
		elements = [elements]


	boxes = []
	opt = Options()
	opt.DetailLevel = ViewDetailLevel.Fine
	
	solids,boxes = [],[]
	for element in elements:
		instGeo = element.get_Geometry(opt)
		
		for ig in instGeo:
			if ig.GetType() == Solid:
				box = GeoBox(ig)
				boxes.append(box)
				solids.append(ig)
			else:			
				geo = DS.List.Flatten(list(ig.GetInstanceGeometry()))
				for g in geo:
					if g.GetType() == Solid:
						box = g.GetBoundingBox()
						if box.Max.X < 99999:					
							box = GeoBox(g)
							boxes.append(box)
							solids.append(g)
					
	sumBox = SumBoxes(boxes)
	center = box.Max.Add(box.Min).Multiply(0.5)
	
	rotatedBoxes = []
	
	for i in range(len(boxes)):
	
		t = Transform.CreateRotationAtPoint(XYZ.BasisZ,-angle,center)
		g = SolidUtils.CreateTransformed(solids[i],t)
		rotatedBoxes.append(GeoBox(g))
					
	
	sumBox = SumBoxes(rotatedBoxes)

	minp = sumBox.Min
	maxp = sumBox.Max
	
	h = maxp.Z-minp.Z
	
	p1 = minp
	p3 = XYZ(maxp.X,maxp.Y,minp.Z)
	p2 = XYZ(minp.X,maxp.Y,minp.Z)
	p4 = XYZ(maxp.X,minp.Y,minp.Z)
	
	t2 = Transform.CreateRotationAtPoint(XYZ.BasisZ,angle,center)
	points = [t2.OfPoint(p).ToPoint() for p in [p1,p2,p3,p4]]
	
	poly = DG.PolyCurve.ByPoints(points,True)
	
	# New code...
	rvtCrvLoop = CurveLoop()
	for c in DG.PolyCurve.Curves(poly):
		rvtCrvLoop.Append(c.ToRevitType())		

	loopList = System.Collections.Generic.List[CurveLoop]()
	loopList.Add(rvtCrvLoop)
	
	rSld = GeometryCreationUtilities.CreateExtrusionGeometry(loopList, XYZ(0,0,1), h)
	# End new code...
	
	solid = poly.ExtrudeAsSolid(DG.Vector.ZAxis(),h*304.8)
	
	return [solid, rSld]
	
	
angle = math.radians(IN[1])
elements = UnwrapElement(IN[0])
invert = IN[2] # New Param...

# Code Removed...
#OUT = RotatedBox(elements,angle)

# New Code...
solids = RotatedBox(elements,angle)
dynSolid = solids[0]
rvtSolid = solids[1]

filter = ElementIntersectsSolidFilter(rvtSolid, invert)
elems = FilteredElementCollector(doc).WherePasses(filter).ToElements()

OUT = elems, dynSolid