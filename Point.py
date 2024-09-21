def check_point_duplicates(point_list1, point_list2):
    duplicates = []
    unique_points = []

    for p1 in point_list1:
        is_duplicate = False
        for p2 in point_list2:
            if p1.X == p2.X and p1.Y == p2.Y and p1.Z == p2.Z:
                duplicates.append(p1)
                is_duplicate = True
                break
        if not is_duplicate:
            unique_points.append(p1)
    return [duplicates, unique_points]

OUT = check_point_duplicates(pts1, pts2)
------------------------------------------------------------------------------------------------
align point
highPoint = IN[1].Z
targetPoint = IN[0]
targetPoint = XYZ(targetPoint.X, targetPoint.Y, highPoint)
OUT = targetPoint
highPoint = IN[1].Z
targetPoint = IN[0][0]
x = targetPoint.X
y = targetPoint.Y
z = highPoint
OUT = Point.ByCoordinates(x,y,z)
------------------------------------------------------------------------------------------------
def get_xyz_from_detail_line(detail_line):
    # Access the curve of the DetailLine
    curve = detail_line.GeometryCurve

    # Convert the curve to a Line object
    line = curve.ToProtoType()

    # Get the start and end points of the Line
    start_point = line.StartPoint()
    end_point = line.EndPoint()

    # Create XYZ objects from the start and end points
    start_xyz = XYZ(start_point.X, start_point.Y, start_point.Z)
    end_xyz = XYZ(end_point.X, end_point.Y, end_point.Z)

    # Return the XYZ coordinates
    return start_xyz, end_xyz
def sortedPoints(points):
    # Sort points first by X, then Y, then Z coordinates
    points = sorted(points, key=lambda point: (round(point.X, 3), round(point.Y, 3), round(point.Z, 3)))
    return points

def sortedPointsWithIndex(points):
    # Enumerate points to pair each point with its original index
    indexedPoints = list(enumerate(points))
    # Sort indexed points based on rounded X, Y, and Z coordinates
    sortedIndexedPoints = sorted(indexedPoints, key=lambda idxPt: (
        round(idxPt[1].X, 3), 
        round(idxPt[1].Y, 3), 
        round(idxPt[1].Z, 3)
    ))
    # Unpack sorted points and their indices
    sortedPoints = [pt for idx, pt in sortedIndexedPoints]
    indices = [idx for idx, pt in sortedIndexedPoints]
    return sortedPoints, indices

#public
def sortPointsByAxis(points, axis='X', descending=False):
    # Define a lambda function to extract the specified axis value from a point
    key_function = lambda point: getattr(point, axis)
    # Sort the points based on the specified axis
    sorted_points = sorted(points, key=key_function, reverse=descending)
    return sorted_points

def find_farthest_and_nearest_points(points):
    farthest_point = None
    nearest_point = None
    farthest_distance = 0
    nearest_distance = float('inf')

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = math.sqrt((points[i].X - points[j].X)**2 + (points[i].Y - points[j].Y)**2 + (points[i].Z - points[j].Z)**2)
            if distance > farthest_distance:
                farthest_distance = distance
                farthest_point = points[i], points[j]
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_point = points[i], points[j]
    return farthest_point, nearest_point
def getPointFromConnectors(connectors , objectType='xyz'):
    points = []
    for conn in connectors:
      if objectType != 'xyz':
         points.append(conn.Origin.ToPoint())
      points.append(conn.Origin)
    return points

class PointCalculator:
    def __init__(self, point_pairs):
        """
        Initializes PointCalculator with a list of point pairs.
        Args:
            point_pairs (list): The list of point pairs. Each pair contains two points (point1, point2).
        """
        self.point_pairs = point_pairs

    @property
    def calculate_midpoints(self):
        """
        Calculates the midpoints for each point pair.
        Returns:
            list: The list of corresponding midpoints (XYZ objects).
        """
        midpoints = []
        for pair in self.point_pairs:
            point1, point2 = pair
            x = (point1.X + point2.X) / 2
            y = (point1.Y + point2.Y) / 2
            z = (point1.Z + point2.Z) / 2
            midpoint = XYZ(x, y, z)
            midpoints.append(midpoint)
        return midpoints

    @property
    def left_points(self):
        """
        Returns the left points in each point pair.
        Returns:
            list: The list of left points (XYZ objects).
        """
        left_points = [pair[0] for pair in self.point_pairs]
        return left_points

    @property
    def right_points(self):
        """
        Returns the right points in each point pair.
        Returns:
            list: The list of right points (XYZ objects).
        """
        right_points = [pair[1] for pair in self.point_pairs]
        return right_points

    @property
    def distance(self):
        """
        Calculates the distance between each point pair.
        Returns:
            list: The list of distances between the points.
        """
        distances = []
        for pair in self.point_pairs:
            point1, point2 = pair
            distance = point1.DistanceTo(point2)
            distances.append(distance)
        return distances

    @property
    def max_point(self):
        """
        Finds the maximum point among all points.
        Returns:
            XYZ: The maximum point.
        """
        all_points = [point for pair in self.point_pairs for point in pair]
        max_x = max(point.X for point in all_points)
        max_y = max(point.Y for point in all_points)
        max_z = max(point.Z for point in all_points)
        max_point = XYZ(max_x, max_y, max_z)
        return max_point

    @property
    def min_point(self):
        """
        Finds the minimum point among all points.
        Returns:
            XYZ: The minimum point.
        """
        all_points = [point for pair in self.point_pairs for point in pair]
        min_x = min(point.X for point in all_points)
        min_y = min(point.Y for point in all_points)
        min_z = min(point.Z for point in all_points)
        min_point = XYZ(min_x, min_y, min_z)
        return min_point

    @property
    def sort_points(self, axis="X"):
        """
        Sorts the points in each point pair in ascending order based on the specified axis.
        Args:
            axis (str): The axis to sort the points ("X", "Y", or "Z"). Default is "X".
        """
        for pair in self.point_pairs:
            pair.sort(key=lambda point: getattr(point, axis))

    @property
    def get_midpoint_index(self, midpoint):
        """
        Returns the index of the given midpoint in the list of midpoints.
        Args:
            midpoint (XYZ): The midpoint to find the index of.
        Returns:
            int: The index of the midpoint. Returns -1 if not found.
        """
        midpoints = self.calculate_midpoints
        for i, point in enumerate(midpoints):
            if point == midpoint:
                return i
        return -1

    @property
    def create_vectors(self):
        """
        Creates vectors from left to right for each point pair.
        Returns:
            list: The list of corresponding vectors (XYZ objects).
        """
        vectors = []
        for pair in self.point_pairs:
            point1, point2 = pair
            vector = point2 - point1
            vectors.append(vector)
        return vectors

    @staticmethod
    def create_lines( point_pairs, doc):
        """
        Creates lines from each point pair in the Revit document.
        Args:
            doc (Document): The Revit document to create the lines in.
        Returns:
            list: The list of created Line objects.
        """
        TransactionManager.Instance.EnsureInTransaction(doc)
        midpoints = PointCalculator.calculate_midpoints
        lines = []
        for pair in point_pairs:
            point1, point2 = pair
            start_point = XYZ(point1.X, point1.Y + 1, point1.Z)
            end_point = XYZ(point2.X, point2.Y + 1 , point2.Z)
            line = Line.CreateBound(start_point, end_point)
            lines.append(line)
            doc.Create.NewDetailCurve(doc.ActiveView, line)
        TransactionManager.Instance.TransactionTaskDone()
        return lines
class GenerationPoint:
    def __init__(self):
        self.params = "params"
    def pickPoints(self, num_points, offset):
        uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
        points = []
        try:
            while True:
                base_point = uidoc.Selection.PickPoint("Select Base Point")
                group = []
                group.append(base_point)  # add original points into group
                for _ in range(num_points - 1):
                    offset_point = self.offset_point(group[-1], offset/304.84)  # Offset from point before
                    group.append(offset_point)
                points.append(group)
        except Autodesk.Revit.Exceptions.OperationCanceledException:
            pass
        return points
    
    def offset_point(self, point, offset):
        new_point = XYZ(point.X, point.Y - offset, point.Z)
        return new_point

    generationPoint = GenerationPoint()
    grouped_points = generationPoint.pickPoints(4, 1000)
    re = []
    for i, group in enumerate(grouped_points):
        re.append(group)
    OUT = re

def sortPoints(points):
	points = sorted(points, key = lambda points: points.X and points.Y and points.Z)
	return points[0], points[-1]

def chunks(l,n):
    n = max(1,n)
    return (l[i:i+n] for i in range(0, len(l), n))
class GenerationPoint:
    def __init__(self):
        pass
    @property
    def pickPoints(self):
        points = []
        try:
            while True:
                base_points = uidoc.Selection.PickPoint("Select Base Points")
                points.append(base_points)
        except Autodesk.Revit.Exceptions.OperationCanceledException:
            pass
        return points
    @staticmethod
    def generate_square(points):
        square_points = []
        for i in range(0,len(points),2):
            if i + 1  < len(points):
                point1 = points[i]
                point3 = points[i+1]
                offset_x = point3.X - point1.X
                offset_y = point3.Y - point1.Y
                point2 = XYZ(point1.X + offset_x, point1.Y, point1.Z)
                point4 = XYZ(point3.X - offset_x, point3.Y, point3.Z)
                square_points.append([point1, point2, point3, point4])
        return square_points
    @staticmethod
    def get_points_from_square(points):
        result = []
        for i in range(0, len(points)):
            spPoint = points[i]
            point1 = spPoint[0]
            point2 = spPoint[1]
            point3 = spPoint[2]
            arrPoints = [point1, point2, point3]
            result.append(arrPoints)
        return result
    @staticmethod
    def pairWise(points):
        paired_points = []
        for lst in points:
            for i in range(len(lst)-1):
                if(i + 1 > len(lst)): break
                pair = [lst[i], lst[i+1]]
                paired_points.append(pair)
        return paired_points

----------------------------------------------------------------
#public
def getPointByLines(lines):
    points = []
    for line in lines:
        start_point = Point.ByCoordinates(line.StartPoint.X, line.StartPoint.Y, line.StartPoint.Z)
        end_point = Point.ByCoordinates(line.EndPoint.X, line.EndPoint.Y, line.EndPoint.Z)
        points.append([start_point, end_point])
    return points
#public
def getXYZByPoints(points):
    xyz_coordinates = []
    for point in points:
        x = round(point.X, 3)
        y = round(point.Y, 3)
        z = round(point.Z, 3)
        xyz_coordinates.append(XYZ(x, y, z))
    return xyz_coordinates
def getXYZFromPoint(point):
    return XYZ(line.StartPoint.X, line.StartPoint.Y, line.StartPoint.Z)
#public
def pointToMiddlePoint(start_point, end_point):
    # Calculate the middle point as a Point
    middle_point = Point.ByCoordinates(
        (start_point.X + end_point.X) / 2,
        (start_point.Y + end_point.Y) / 2,
        (start_point.Z + end_point.Z) / 2
    )
    return middle_point
#public
def vectorToPoint(vectors):
	result = []
	for vector in vectors:
		x = vector.X
		y = vector.Y
		z = vector.Z
		# Create a point using the vector's coordinates
		point = Point.ByCoordinates(x, y, z)
		result.append(point)
	return result
#public
def pointToVector(point):
    x = point.X
    y = point.Y
    z = point.Z
    # Create a vector using the point's coordinates
    vector = Vector.ByCoordinates(x, y, z)
    return vector
#public
def getPointsByLines(lines):
    points_dict = {'start': [], 'middle': [], 'end': []}
    for line in lines:
        start_point = line.StartPoint
        end_point = line.EndPoint

        # Convert points to vectors
        start_vector = pointToVector(start_point)
        end_vector = pointToVector(end_point)

        # Convert vectors to points for start and end
        start_point_converted = Point.ByCoordinates(start_vector.X, start_vector.Y, start_vector.Z)
        end_point_converted = Point.ByCoordinates(end_vector.X, end_vector.Y, end_vector.Z)

        # Calculate the middle point as a Point
        middle_point = pointToMiddlePoint(start_point, end_point)

        points_dict['start'].append(start_point_converted)
        points_dict['middle'].append(middle_point)
        points_dict['end'].append(end_point_converted)
    return points_dict
#public
def getX_Y_Z(vectors):
	cX, cY, cZ = [], [], []
	for vector in vectors:
		x = vector.X
		y = vector.Y
		z = vector.Z
		cX.append(x)
		cY.append(y)
		cZ.append(z)
	result_dict = {"x" : cX, "y": cY, "z": cZ}
	return result_dict

def getLocationXYZ(element): # Get XYZ of element.    
    point = element.Location
    return XYZ(point.X, point.Y, point.Z)

def sortXYZ(lstXyz):
    # Sort lstXyz by coordinates X, then Y, then Z
    sortedIndices = sorted(enumerate(lstXyz), key=lambda point: (point[1][0], point[1][1], point[1][2]))
    indices = [index for index, _ in sortedIndices]
    sortedPoints = [point for _, point in sortedIndices]
    return indices, sortedPoints

def findExtremePoint(points, coordinate='Z', findMin=True):
    if not points:
        return None
    compare = min if findMin else max
    if coordinate not in ['X', 'Y', 'Z']:
        raise ValueError("Coordinate must be 'X', 'Y', or 'Z'")
    extremePoint = points[0]
    for point in points:
        # Get the current coordinate value of the point being checked
        currentAttribute = getattr(point, coordinate)
        # Get the coordinate value of the current extreme point
        extremeAttribute = getattr(extremePoint, coordinate)
        # Update 'extremePoint' if the current point's value is more extreme
        if compare(currentAttribute, extremeAttribute) == currentAttribute:
            extremePoint = point
    return extremePoint

def findExtremePointOnLine(line, coordinate='Z', findMin=True):
    if not line:
        return None
    # Retrieve start and end points of the line
    startPoint = line.StartPoint
    endPoint = line.EndPoint
    compare = min if findMin else max
    if coordinate not in ['X', 'Y', 'Z']:
        raise ValueError("Coordinate must be 'X', 'Y', or 'Z'")
    # Extract the relevant coordinate from each point
    startCoord = getattr(startPoint, coordinate)
    endCoord = getattr(endPoint, coordinate)
    # Determine which point is the extreme point
    extremePoint = startPoint if compare(startCoord, endCoord) == startCoord else endPoint
    return extremePoint


def offsetZPoints(points, zOffset):
    updatedPoints = []
    for point in points:
        startPoint = point['start_point']
        endPoint = point['end_point']
        
        # Update the Z-coordinate of the start and end points
        startPointUpdated = [startPoint[0], startPoint[1], startPoint[2] + zOffset]
        endPointUpdated = [endPoint[0], endPoint[1], endPoint[2] + zOffset]
        
        updatedPoint = {
            'start_point': startPointUpdated,
            'end_point': endPointUpdated
        }
        updatedPoints.append(updatedPoint)
    return updatedPoints
    # pointDicts = IN[0]
    # zOffset = 50/304.84
    # OUT = offsetZPoints(pointDicts, zOffset)

def convertToXYZ(pointsList):
    """
    Converts a nested list of point coordinates into XYZ objects.
    Parameters:
    pointsList (list of lists): A nested list where each sub-list contains X, Y, Z coordinates of a point.
    Returns:
    list of XYZ: A list of XYZ objects representing the points.
    """
    xyzPoints = []
    for point in pointsList:
        # Create an XYZ object for each sublist
        xyzPoint = XYZ(point[0], point[1], point[2])
        xyzPoints.append(xyzPoint)
    
    return xyzPoints
    nums = IN[0]
    OUT = [convertToXYZ(num) for num in nums]

def findMatchingPoints(lines, points):
    matchingPoints = []
    for line in lines:
        startPoint = line.StartPoint
        endPoint = line.EndPoint
        for point in points:
            if startPoint.IsAlmostEqualTo(point):
                matchingPoints.append(point)
            if endPoint.IsAlmostEqualTo(point):
                matchingPoints.append(point)
    return matchingPoints

def checkAxisMovement(points):
    # Giả định rằng danh sách points chứa ít nhất hai điểm để so sánh
    if len(points) < 2:
        return "Không đủ điểm để kiểm tra."

    # Lấy tọa độ của điểm đầu tiên và điểm thứ hai, và làm tròn đến 4 chữ số thập phân
    x1, y1, z1 = round(points[0].X, 4), round(points[0].Y, 4), round(points[0].Z, 4)
    x2, y2, z2 = round(points[1].X, 4), round(points[1].Y, 4), round(points[1].Z, 4)

    # Kiểm tra sự khác biệt trong các tọa độ đã được làm tròn và xác định hướng di chuyển
    if x1 != x2 and y1 == y2 and z1 == z2:
        if x2 > x1:
            return "X"
        else:
            return "-X"
    elif x1 == x2 and y1 != y2 and z1 == z2:
        if y2 > y1:
            return "Y"
        else:
            return "-Y"
    elif x1 == x2 and y1 == y2 and z1 != z2:
        if z2 > z1:
            return "Z"
        else:
            return "-Z"
    else:
        return "Di chuyển theo nhiều trục hoặc không có trục nào được di chuyển rõ ràng."

    # # Áp dụng hàm vào danh sách các phần tử
    # elements = unwrapInput(IN[1])
    # OUT = checkAxisMovement(elements)

def uniquePointsByLines(lines):
    points = {}
    for line in lines:
        start = line.StartPoint
        end = line.EndPoint
        startKey = (round(start.X, 2), round(start.Y, 2), round(start.Z, 2))
        if startKey not in points:
            points[startKey] = start
        # Kiểm tra và thêm điểm end vào dictionary nếu chưa có
        endKey = (round(end.X, 2), round(end.Y, 2), round(end.Z, 2))
        if endKey not in points:
            points[endKey] = end
    return points.values()

def getLengthOfLines(lines):
    length = 0
    for line in lines:
        length += line.Length
    return length

def movePoints(points, targetZ=0, targetX=0, targetY=0):
    movedPoints = []
    for point in points:
        movedPoint = Point.Add(point, Vector.ByCoordinates(targetX, targetY, targetZ))
        movedPoints.append(movedPoint)
    return movedPoints
    # targetX = IN[1]
    # targetY = IN[2]
    # targetZ = IN[3]

    # elements = getList(IN[0])
    # movedPointsList = movePoints(elements,targetZ, targetX, targetY)
    # OUT = movedPointsList

def findIntersecPoints(lines):
    intersecPoints = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            intersection = lines[i].Intersect(lines[j])
            if intersection:
                intersecPoints.extend(intersection)
    uniquePoints = list(set(intersecPoints))
    return  uniquePoints

def removeDuplicatePoints(points):
    # Create a dictionary to hold unique points
    uniquePoints = {}
    for point in points:
        # Use a tuple of coordinates as the key for the dictionary
        key = (round(point.X, 3), round(point.Y, 3), round(point.Z, 3))  # Round to avoid floating-point arithmetic issues
        if key not in uniquePoints:
            uniquePoints[key] = point
    # Return a list of non-duplicate points
    return list(uniquePoints.values())

def getMinAndMaxPoints(points):
    result = [{"X": p.X, "Y": p.Y, "Z": p.Z} for p in points]
    min_x = min(p['X'] for p in result)
    max_x = max(p['X'] for p in result)
    min_y = min(p['Y'] for p in result)
    max_y = max(p['Y'] for p in result)
    return min_x, max_x, min_y, max_y

def offsetPoints(pointsDict, dis):
    minX = min(p['x'] for p in pointsDict)
    maxX = max(p['x'] for p in pointsDict)
    minY = min(p['y'] for p in pointsDict)
    maxY = max(p['y'] for p in pointsDict)

    leftOffset = []
    rightOffset = []
    bottomOffset = []
    topOffset = []
    noOffset = []

    for p in pointsDict:
        if p['x'] == minX:  # left points
            leftOffset.append({'x': p['x'] - dis, 'y': p['y'], 'z': p['z']})
        elif p['x'] == maxX:  # right points
            rightOffset.append({'x': p['x'] + dis, 'y': p['y'], 'z': p['z']})
        elif p['y'] == minY:  # bottom points
            bottomOffset.append({'x': p['x'], 'y': p['y'] - dis, 'z': p['z']})
        elif p['y'] == maxY:  # top points
            topOffset.append({'x': p['x'], 'y': p['y'] + dis, 'z': p['z']})
        else:
            noOffset.append(p)

    leftTargetPoints = [Point.ByCoordinates(p['x'], p['y'], p['z']) for p in leftOffset]
    rightTargetPoints = [Point.ByCoordinates(p['x'], p['y'], p['z']) for p in rightOffset]
    bottomTargetPoints = [Point.ByCoordinates(p['x'], p['y'], p['z']) for p in bottomOffset]
    topTargetPoints = [Point.ByCoordinates(p['x'], p['y'], p['z']) for p in topOffset]

    return leftTargetPoints, rightTargetPoints, bottomTargetPoints, topTargetPoints
    # # Sử dụng hàm
    # pointsDict = getList(IN[0])
    # dis = IN[1]

    # OUT = offset_points(pointsDict, dis)

def offsetPointsByPoints(points, dis, typeAxis):
    newPoints = []
    for p in points:
        if typeAxis == 'x':
            px = p.X + dis
            py, pz = p.Y, p.Z
            point = Point.ByCoordinates(px, py, pz)
        elif typeAxis == 'y':
            py = p.Y + dis
            px, pz = p.X, p.Z
            point = Point.ByCoordinates(px, py, pz)
        else:
            pz = p.Z + dis
            px, py = p.X, p.Y
            point = Point.ByCoordinates(px, py, pz)
        newPoints.append(point)
    return newPoints