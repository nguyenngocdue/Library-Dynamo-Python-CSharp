def get_pipe_endpoints(pipe_refs):
    endpoints = []
    for ref in pipe_refs:
        pipe = doc.GetElement(ref) # Get the pipe object from the reference
        location_curve = pipe.Location.Curve # Get the location curve of the pipe
        start_point = location_curve.GetEndPoint(0) # Get the start point
        end_point = location_curve.GetEndPoint(1) # Get the end point
        endpoints.append([start_point, end_point])
    return endpoints
def get_mep_connections(elements):
    result = []
    for element in elements:
        try:
            connectors = element.MEPModel.ConnectorManager.Connectors
        except:
            try:
                connectors = element.ConnectorManager.Connectors
            except:			
                connectors = []
        result.append([x for x in connectors])
    return result
def getPointFromConnector(connectors):
    points = []
    for conn in connectors:
        points.append(conn.Origin.ToPoint())
    return points
def getToVectorFromConnector(connectors):
    vector = []
    for conn in connectors:
        vector.append(conn.CoordinateSystem.BasisZ.ToVector())
    return vector
def getSinglePoints(points):
    non_intersect_points = []
    intersect_points = []
    for idx1, p1 in enumerate(points):
        is_intersected = False
        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            if abs(round(p1.Y)) == abs(round(p2.Y)):
                intersect_points.append(p2)
                is_intersected = True
            else:
                break
        if  is_intersected == False:
            return idx2, p2,
            # non_intersect_points.append(p1)
    return non_intersect_points
    
def getSinglePoints(points, line):
    unique_points  = []
    index = []
    for idx, point in enumerate(points):
        intersect = line.DoesIntersect(point)
        if not intersect:
            unique_points.append(point)
            index.append(idx)
    return unique_points,index

def getConnectors(elements):
   listOut = []
   for element in elements:
      try:
         connectors = element.MEPModel.ConnectorManager.Connectors
      except:
         try:
            connectors = element.ConnectorManager.Connectors
         except:	"error"
      listOut.append([x for x in connectors])
   return listOut

def getPointFromConnectors(connectors , objectType='xyz'):
    points = []
    for conn in connectors:
      if objectType != 'xyz':
         points.append(conn.Origin.ToPoint())
      points.append(conn.Origin)
    return points

def remove_element(element):
    doc = DocumentManager.Instance.CurrentDBDocument
    TransactionManager.Instance.EnsureInTransaction(doc)
    doc.Delete(element.Id)
    TransactionManager.Instance.TransactionTaskDone()
    return "Element removed successfully"

def sortPoints(points):
	points = sorted(points, key = lambda points: points.X and points.Y and points.Z)
	return points[0], points[-1]



