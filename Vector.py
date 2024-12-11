def getVectorsByLines(lines):
	return [XYZ(i.Direction.X,i.Direction.Y, i.Direction.Z)  for i in lines]

def getCurveNormalsByLines(lines):
	return [i.Normal  for i in lines]

def getXYZCurveNormalsByLines(lines):
	return [XYZ(i.Normal.X,i.Normal.Y,i.Normal.Z)  for i in lines]
	
def getOriginOfDbPFaces(dbPlanarFaces):
    result = []
    for pl in dbPlanarFaces:
        result.append(pl.Origin)
    return result

def createXYZVectorsFromPoints(points):
    vectors = []
    for point in points:
        start_point = point['start_point']
        end_point = point['end_point']
        # Create a vector by subtracting the start point from the end point
        vector = XYZ(end_point[0] - start_point[0], end_point[1] - start_point[1], end_point[2] - start_point[2])
        vectors.append(vector)
    return vectors

def calculateVectorByLstXYZ(xyz1, xyz2):
    x1, y1, z1 = xyz1.X, xyz1.Y, xyz1.Z
    x2, y2, z2 = xyz2.X, xyz2.Y, xyz2.Z
    vector = (x2 - x1, y2 - y1, z2 - z1)
    return vector


pointDicts = IN[0]
OUT = createXYZVectorsFromPoints(pointDicts)