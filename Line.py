lines = UnwrapElement(IN[0])
# Get the start and end points of each line
def getPointsByLines(lines):
	points = []
	for line in lines:
		start_point = line.StartPoint
		end_point = line.EndPoint
		points.append(start_point)
		points.append(end_point)
	return points

# Output the points
OUT = getPointsByLines(lines)

def getPointsByLine(line):
    start_point = line.StartPoint
    end_point = line.EndPoint
    return start_point, end_point

def getPointsByLine(line):
    start_point = line.StartPoint
    end_point = line.EndPoint
    return {"start_point": start_point, "end_point": end_point}

def getXYZByLine(line):
    start_point = line.StartPoint
    end_point = line.EndPoint
    start_point_xyz = {'X': start_point.X, 'Y': start_point.Y, 'Z': start_point.Z}
    end_point_xyz = {'X': end_point.X, 'Y': end_point.Y, 'Z': end_point.Z}
    return {'start_point': start_point_xyz, 'end_point': end_point_xyz}

def getXYZByLine(line):
    start_point = line.StartPoint
    end_point = line.EndPoint
    start_point_xyz = [start_point.X, start_point.Y, start_point.Z]  # Start point coordinates as a list
    end_point_xyz = [end_point.X, end_point.Y, end_point.Z]          # End point coordinates as a list
    return [start_point_xyz, end_point_xyz]
lines = IN[0]  # The input list of lines from Dynamo
OUT = [getXYZByLine(l) for l in lines]  # Apply the function to each line and collect the results


def getXYZByLine(line):
    start_point = line.StartPoint
    end_point = line.EndPoint
    start_point_xyz = [start_point.X, start_point.Y, start_point.Z]  # Start point coordinates as a list
    end_point_xyz = [end_point.X, end_point.Y, end_point.Z]          # End point coordinates as a list
    return {'start_point': start_point_xyz, 'end_point': end_point_xyz}

lines = IN[0]  # The input list of lines from Dynamo
OUT = [getXYZByLine(l) for l in lines]  # Apply the function to each line and collect the results in a dictionary format

------------------------------------------------------------------------------------------------
def get_higher_point(point1, point2):
    # Compare the Z-coordinates of the points
    if point1.Z > point2.Z:
        higher_point = point1
    elif point2.Z > point1.Z:
        higher_point = point2
    else:
        higher_point = None  # Points have the same elevation
    
    return higher_point
------------------------------------------------------------------------------------------------
start_point = XYZ(round(start_point.X/unit),round(start_point.Y/unit),round(start_point.Z/unit) )
end_point = XYZ(round(end_point.X/unit),round(end_point.Y/unit),round(end_point.Z/unit)+(h/unit) )
------------------------------------------------------------------------------------------------
ele = SelectionFilter("Pipes", "Lines")
elSelectAll = uidoc.Selection.PickElementsByRectangle(ele,"Selects")
OUT = [i.GeometryCurve for i in elSelectAll]
------------------------------------------------------------------------------------------------
def get_xyz_from_db_line(db_line):
    # Get the start and end points of the Line
    start_point = db_line.GetEndPoint(0)
    end_point = db_line.GetEndPoint(1)

    # Create XYZ objects from the start and end points
    start_xyz = XYZ(start_point.X, start_point.Y, start_point.Z)
    end_xyz = XYZ(end_point.X, end_point.Y, end_point.Z)

    # Return the XYZ coordinates
    return start_xyz, end_xyz
#public
def getDBLineFormEleLine(elementLines): # Get Revit.DB.Line from Curve Elements
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.View = doc.ActiveView
    ln = []
    for j in elementLines:
    	ln.append(UnwrapElement(j).ToRevitType())
    return ln

def getCenterPointOfLine(line):
    if not line:
        return None
    
    # Retrieve start and end points of the line
    startPoint = line.StartPoint
    endPoint = line.EndPoint
    
    # Calculate the coordinates of the center point
    centerX = (startPoint.X + endPoint.X) / 2
    centerY = (startPoint.Y + endPoint.Y) / 2
    centerZ = (startPoint.Z + endPoint.Z) / 2
    
    # Create and return the center point
    centerPoint = Point.ByCoordinates(centerX, centerY, centerZ)
    return centerPoint