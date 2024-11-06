def getGeoElement(ele):
    geo = []
    opt = Options()
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.DetailLevel = ViewDetailLevel.Fine
    geometry = ele.get_Geometry(opt)
    return geometry

def getDBSolidByDBGeometries(dbGeoes):
    dbSolids = []
    for geo in dbGeoes:
        if geo.GetType().ToString() == 'Autodesk.Revit.DB.Solid' and geo.Volume > 0:
            dbSolids.append(geo)
    return dbSolids

def getDBLineByDBGeometries(dbGeoes):
    dbLines = []
    for geo in dbGeoes:
        if geo.GetType().ToString() == 'Autodesk.Revit.DB.Line':
            dbLines.append(geo)
    return dbLines

def getDBPlanarFacesByDBSolids(dbSolids):
    planarFaces = []
    for sol in dbSolids:
        faces = sol.Faces
        planarFaces.append(faces)
    return planarFaces

def isParalel(p, q):
    return p.CrossProduct(q).IsZeroLenth() #=> true/ false

def getVerticalDbPlanarfaces(dbPlanarFaces):
    dbVerPlanarFaces = []
    y = XYZ.BasisY
    for face in dbPlanarFaces:
        normal = face.FaceNormal
        isParalel = isParalel(y,normal)
        if isParalel:
            dbVerPlanarFaces.append(face)
    return dbVerPlanarFaces

def getMaxLines(dBLines):
    lengths = []
    for l in dBLines:
        lengths.append(l.Length)
    maxDbLines = []
    for dbLine in dBLines:
        if dbLine.Length == max(lengths):
            maxDbLines.append(dbLine)
    return maxDbLines

def getRightDbPlanarFaces(dbPlanarFaces):
    rightDbPlanarFaces = []
    direct = view.RightDirection
    for planarFace in dbPlanarFaces:
        faceNormal = planarFace.FaceNormal
        if faceNormal.IsAlmostEqualTo(direct):
            rightDbPlanarFaces.append(planarFace)
    return rightDbPlanarFaces

def getTopOrBotPlanarFaces(dbPlanarFaces, isTop=True):
    tbDbPlanarFaces = []
    for p in dbPlanarFaces:
        if isTop:
            if p.FaceNormal.Z > 0:
                tbDbPlanarFaces.append(p)
        else:
            if p.FaceNormal.Z < 0:
                tbDbPlanarFaces.append(p)
    return tbDbPlanarFaces