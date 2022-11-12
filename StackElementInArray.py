data = [1,2,3,4,5,6,7,8,9,10]
ldata = [[1,2,3],[4,5,6],[7,8,9,10]]

def totalSumOfSum (data):
    total = data[0]
    if len(data) >= 2:
        sum = data[0] + data[1]
        for i in range(2, len(data), 1):
            sum = sum + data[i]
            total = sum
    return total


value = totalSumOfSum(data)

result = []
for index in range(0, len(ldata), 1):
    data = ldata[index]
    result.append(totalSumOfSum(data))

print(result)