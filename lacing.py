a = [1,2,3]
b = [4,5,-6,-7,8,9]
re = []
n = 0

for i in a:
    r1 = []
    for j in b:
        val = i*j
        if val > 0:
            r1.append(val)
    re.append(r1)
print (re)