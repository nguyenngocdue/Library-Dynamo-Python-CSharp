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
def sortPoints(points):
	points = sorted(objects, key = lambda objects: objects.X and objects.Y and objects.Z)
	return points[0], points[-1]

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