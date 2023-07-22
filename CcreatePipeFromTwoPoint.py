import clr
import System
import math
from System.Collections.Generic import *

import os
import sys
import logging
sys.path.append(r"C:\\Users\\NGUYEN NGOC DUE\\.vscode\\ironpython-stubs-master\\release\\stubs.min\\pyrevit\\coreutils")
sys.path.append(os.path.dirname(__file__))

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

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

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