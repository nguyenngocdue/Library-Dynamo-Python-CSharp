def getVectorsByLines(lines):
	return [XYZ(i.Direction.X,i.Direction.Y, i.Direction.Z)  for i in lines]

def getCurveNormalsByLines(lines):
	return [i.Normal  for i in lines]

def getXYZCurveNormalsByLines(lines):
	return [XYZ(i.Normal.X,i.Normal.Y,i.Normal.Z)  for i in lines]
