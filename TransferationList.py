lstEle = UnwrapElement(IN[1])
if isinstance(lstEle,list):
    elements = UnwrapElement(lstEle)
else:
    elements = [UnwrapElement(lstEle)]