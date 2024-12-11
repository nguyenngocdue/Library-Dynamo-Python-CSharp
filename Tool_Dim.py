Solve 1:
# dim.ValueOverride = replace_text

Solve 2:
# dimensions = getList(IN[0])
# # Danh sách lưu kết quả (đơn vị mm)
# dimension_values_mm = []
# # Hệ số chuyển đổi từ feet sang mm
# feet_to_mm = 304.8
# # Duyệt qua từng Dimension
# for dim in dimensions:
#     if isinstance(dim, Dimension):  # Kiểm tra nếu element là Dimension
#         # Kiểm tra nếu Dimension có các đoạn (segments)
#         if dim.Segments:
#             segment_values_mm = []
#             for segment in dim.Segments:
#                 value_mm = round(segment.Value * feet_to_mm, 2)  # Chuyển đổi và làm tròn đến 2 chữ số thập phân
#                 segment_values_mm.append(value_mm)
#             dimension_values_mm.append(segment_values_mm)  # Thêm các giá trị vào danh sách
#         else:
#             # Nếu không có segments, chuyển đổi giá trị của toàn bộ Dimension
#             value_mm = round(dim.Value * feet_to_mm, 2)  # Làm tròn đến 2 chữ số thập phân
#             dimension_values_mm.append(value_mm)
# # Xuất kết quả
# OUT = dimension_values_mm
