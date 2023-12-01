#public
def is_array(obj):
    return "List" in obj.__class__.__name__
#public
def get_array_rank(array):
    if is_array(array):
        return 1 + max(get_array_rank(item) for item in array)
    else:
        return 0

def flatten_to_1d(arr):
    result = []
    def recursive_flatten(subarray):
        for item in subarray:
            if is_array(item):
                recursive_flatten(item)
            else:
                result.append(item)

    recursive_flatten(arr)
    return result
# public
def getValueByKeyObject(keys, objects):
    arrKeys, values = [], []
    for k in keys:
        if k in objects.keys():
            arrKeys.append(k)
            values.append(objects[k])
    return arrKeys, values
