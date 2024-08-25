def unwrapInput(inputValue):
    if isinstance(inputValue, list):
        return UnwrapElement(inputValue)
    else:
        return [UnwrapElement(inputValue)]
    
elements = unwrapInput(IN[0])
