#public
def getXYZOfPipes(pipe_refs):
    xyz = []
    for ref in pipe_refs:
        pipe = doc.GetElement(ref) # Get the pipe object from the reference
        location_curve = pipe.Location.Curve # Get the location curve of the pipe
        start = location_curve.GetEndPoint(0) # Get the start point
        end = location_curve.GetEndPoint(1) # Get the end point
        xyz.append([start, end])
    return xyz
#public
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

#public
def get_connector_XYZ(connectors):
	xyz = []
	for conn in connectors:
		location = conn.CoordinateSystem
		xyz.append(location.Origin)
	return xyz
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

class GenerationPipe:
    def __init__(self):
        pass
    @staticmethod
    def create_placeHolder(points, elementIds):
        result = []
        for pts in points:
            if(len(pts)) == 2:
                pipe_start = pts[0]
                pipe_end = pts[1]
                sysTypeId = elementIds[1]
                pipeTypeId = elementIds[0]
                levelId = elementIds[2]
                TransactionManager.Instance.EnsureInTransaction(doc)
                pipe = Autodesk.Revit.DB.Plumbing.Pipe.CreatePlaceholder(doc, sysTypeId, pipeTypeId, levelId, pipe_start, pipe_end)
                TransactionManager.Instance.TransactionTaskDone()
                result.append(pipe)
        return result
    @staticmethod
    def connect_placeHolder(elements):
        result = []
        for ele in elements:
            TransactionManager.Instance.EnsureInTransaction(doc)
            re = Autodesk.Revit.DB.Plumbing.PlumbingUtils.ConnectPipePlaceholdersAtElbow(doc, ele[0].Id, ele[1].Id)
            TransactionManager.Instance.TransactionTaskDone()
            result.append(re)
        return result
    @staticmethod
    def convert_to_pipe(elements):
        pipes = []
        for ele in elements:
            placeholderIds = List[ElementId]([ele[0].Id, ele[1].Id])
            TransactionManager.Instance.EnsureInTransaction(doc)
            pipe = Autodesk.Revit.DB.Plumbing.PlumbingUtils.ConvertPipePlaceholders(doc, placeholderIds)
            TransactionManager.Instance.TransactionTaskDone()
            pipes.append(pipe)
        return pipes

    elements = UnwrapElement(IN[0])
    #Step 7:Connect PipePlaceholdersAtElbow
    connPlaceHolder = GenerationPipe.connect_placeHolder(elements)
    #Step 8: convert PipePlaceHolder to Pipe
    pipes = GenerationPipe.convert_to_pipe(elements)

    OUT = pipes

