
framings = IN[0]
walls = IN[1]
floor = IN[2]
dbFramings = IN[3]
dbWalls = IN[4]
dbFloors = IN[5]
#----------------------------------------------------------------
framingsIntersected = []
wallsIntersected = []
floorsIntersected = []

dbElementsHaystack =  dbWalls  + dbFloors + dbFramings
elementsHaystack =  framings  + floor + walls

dbElementNeedle = dbFramings
elementNeedle = framings

for dbFraming, framing in zip(dbElementNeedle, elementNeedle):
    for dbWall, wall in zip(dbElementsHaystack, elementsHaystack):
        instanceSolid = BooleanOperationsUtils.ExecuteBooleanOperation(dbFraming, dbWall, BooleanOperationsType.Intersect)
        if float(instanceSolid.Volume) > 0:
            framingsIntersected.append(wall)
OUT = framingsIntersected, wallsIntersected
