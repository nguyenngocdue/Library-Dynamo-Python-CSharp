#public
def filterDBGeometry(lstGeo):
    objects = {}
    for i in lstGeo:
        type_name = type(i).__name__
        valid_object = False
        if isinstance(i, RDB.Solid):
            valid_object = getattr(i, 'Volume', 0) > 0
        elif isinstance(i, (RDB.GeometryInstance, RDB.Line)):
            valid_object = True  # Adjust this condition based on your requirements
        if valid_object:
            if type_name not in objects:
                objects[type_name] = []
            objects[type_name].append(i)
    return objects
#public
def filterDBGeometry(lstGeo):
    objects = {}
    types = set([str(i.GetType()).split('.')[-1] for i in lstGeo if i is not None])
    objects['Type'] = types
    for geo in lstGeo:
        if geo:
            strType = str(geo.GetType()).split('.')[-1]
            for name in types:
                if name == strType:
                    if name not in objects:
                        objects[name] = []
                    objects[name].append(geo)
                else:
                    if name not in objects:
                        objects[name] = []
    return objects

    