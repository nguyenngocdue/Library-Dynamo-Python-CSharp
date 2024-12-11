import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Function to create planes from lines
def create_planes_from_lines(lines):
    planes = []
    for line in lines:
        # Get the start and end points of the line
        start = line.StartPoint
        end = line.EndPoint

        # Calculate the direction vector of the line
        direction = Vector.ByTwoPoints(start, end).Normalized()

        # Choose an arbitrary vector that is not parallel to the direction
        arbitrary = Vector.ByCoordinates(1, 0, 0) if abs(direction.X) < 0.9 else Vector.ByCoordinates(0, 1, 0)

        # Compute a perpendicular vector
        perpendicular = direction.Cross(arbitrary).Normalized()

        # Compute the normal vector for the plane (perpendicular to both)
        normal = direction.Cross(perpendicular).Normalized()

        # Create a plane at the line's start point with the normal vector
        plane = Plane.ByOriginNormal(start, normal)
        planes.append((plane, start, end, direction))

    return planes

# Function to create surfaces from planes and lines
def create_surfaces_from_planes_and_lines(lines):
    surfaces = []
    for line in lines:
        # Get the start and end points of the line
        start = line.StartPoint
        end = line.EndPoint

        # Calculate the direction vector of the line
        direction = Vector.ByTwoPoints(start, end).Normalized()

        # Calculate line length
        length = start.DistanceTo(end)

        # Define a perpendicular vector for width
        arbitrary = Vector.ByCoordinates(1, 0, 0) if abs(direction.X) < 0.9 else Vector.ByCoordinates(0, 1, 0)
        yAxis = direction.Cross(arbitrary).Normalized()

        # Define the rectangular surface based on the line
        corner1 = start.Add(yAxis.Scale(length / 2))
        corner2 = start.Add(yAxis.Scale(-length / 2))
        corner3 = end.Add(yAxis.Scale(-length / 2))
        corner4 = end.Add(yAxis.Scale(length / 2))

        # Create a surface using the corners
        try:
            surface = Surface.ByPerimeterPoints([corner1, corner2, corner3, corner4])
            surfaces.append(surface)
        except Exception as e:
            surfaces.append(f"Error creating surface: {str(e)}")

    return surfaces

# Example usage
lines = IN[0]  # Input lines from Dynamo

# Generate surfaces from lines
surfaces = create_surfaces_from_planes_and_lines(lines)

# Output the surfaces
OUT = surfaces
