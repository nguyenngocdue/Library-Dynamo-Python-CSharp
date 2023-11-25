def get_array_rank(array):
    if is_array(array):
        return 1 + max(get_array_rank(item) for item in array)
    else:
        return 0


objects = UnwrapElement(IN[1])
typeName = IN[2]

rank = get_array_rank(objects)
if rank == 1:
    OUT = filterGeometryByTypeName(objects, typeName)
elif rank == 2:
    out = []
    for element in objects: out.append(filterGeometryByTypeName(element, typeName))
    OUT = out
else:
    elements = flatten_to_1d(objects)
    OUT = filterGeometryByTypeName(elements, typeName)