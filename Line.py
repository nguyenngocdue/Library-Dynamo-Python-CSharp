lines = UnwrapElement(IN[0])
# Get the start and end points of each line
def getPointByLines(lines):
	points = []
	for line in lines:
		start_point = line.StartPoint
		end_point = line.EndPoint
		points.append(start_point)
		points.append(end_point)
	return points

# Output the points
OUT = getPointByLines(lines)
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