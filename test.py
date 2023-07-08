import clr
import System
import math
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

clr.AddReference("RevitNodes")
import Revit

clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


import os
import sys
import logging
sys.path.append(r"C:\\Users\\NGUYEN NGOC DUE\\.vscode\\ironpython-stubs-master\\release\\stubs.min\\pyrevit\\coreutils")
sys.path.append(os.path.dirname(__file__))



doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

from Autodesk.Revit.DB import XYZ
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

point_pairs = [xyz for xyz in IN[0]]

# Create an instance of PointCalculator with the point pairs
calculator = PointCalculator(point_pairs)

# Calculate the midpoints
midpoints = calculator.calculate_midpoints
distance = calculator.distance
dbLines = PointCalculator.create_lines(point_pairs,doc)


# Print the results

result = []

for i, dis in enumerate(dbLines):
    result.append(dis)
OUT = result