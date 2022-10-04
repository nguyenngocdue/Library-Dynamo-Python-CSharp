#Curve.Length
line = IN[1]
re = []
for i in line:
    re.append(Autodesk.DesignScript.Geometry.Curve.LengthBetweenParameters(i))
OUT = re

#Vector of line : NormalAtParameter
line = IN[1]
re = []
for i in line:
    re.append(Autodesk.DesignScript.Geometry.Curve.NormalAtParameter(i))
OUT = re
#Vector.ByTwoPoints
ip1 = IN[2]
line = IN[1]
re = []
for i,j in zip(ip1, line):
    re.append(Autodesk.DesignScript.Geometry.Vector.ByTwoPoints(i, j))
OUT = re
#Surface.ByPerimeterPoints
OUT = Autodesk.DesignScript.Geometry.Surface.ByPerimeterPoints(IN[1])
