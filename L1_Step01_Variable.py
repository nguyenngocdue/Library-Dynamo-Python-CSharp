import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import*

#input

#CodeMain


#Create Function
def SUMAB(i,j):
    sumx = int(i) +int(j)
    return sumx


a = "Hello World"
b = "200"
c = 100

intByString = int(b)
doublStringbyString = float(b)
check = doublStringbyString == 300

#sumAB = int(b) + int(c)
result = SUMAB(b,c)

#Output
#OUT = a , b ,c , intByString , doublStringbyString, check , sumAB
OUT = result