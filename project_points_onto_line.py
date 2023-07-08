def project_points_onto_line(line, points):
    projected_points = []

    for point in points:
        projection = line.Project(point).XYZPoint
        projected_points.append(projection)

    return projected_points

# Lấy đường thẳng và tập hợp các điểm từ Dynamo (ví dụ)
line = IN[0]  # Đường thẳng (Line)
points = IN[1]  # Tập hợp các điểm (List[XYZ])

projected_points = project_points_onto_line(line, points)

# Trả về kết quả cho Dynamo
OUT = projected_points