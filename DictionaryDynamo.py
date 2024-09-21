def getKeysAndValuesOfDict(myDict):
    if myDict is not None and isinstance(myDict, dict):
        return {'keys' :list(myDict.keys()), 'values' : list(myDict.values())}
    return []

def getAndSetValueAtKeys(myDict, keys, values):
    myKeys = myDict.keys()
    for index, key in enumerate(keys):
        if values[index] is not None: 
            myDict[key] = values[index]
    return myDict