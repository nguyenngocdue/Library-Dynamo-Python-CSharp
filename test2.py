englishNames = [
    "200_Michael Brown",
    "100_Jennifer Lee",
    "100_William Johnson",
    "Elizabeth Wilson",
    "James Davis",
    "Sarah Miller",
    "Joseph Anderson",
    "Jessica Taylor",
    "500_Robert Martinez",
    "500_Karen Hernandez",
    "Charles Jones",
    "300_Margaret Garcia",
    "300_Daniel Wilson",
    "Linda Rodriguez",
    "Christopher Moore",
    "Patricia Perez",
    "Matthew White",
    "700_Nancy Hall",
    "900_Andrew Scott",
    "1000_Maria Gonzalez",
    "abc"
]

# Dictionary to store grouped names
groupedDict = {}
# List to store names that don't have a group
generalGroup = []

for name in englishNames:
    # Check the length condition and extract the key
    if len(name) >= 4:
        groupKey = name[:4]
        # Append to existing group in dictionary or create new group
        if groupKey in groupedDict:
            groupedDict[groupKey].append(name)
        else:
            groupedDict[groupKey] = [name]
    else:
        generalGroup.append(name)

# Remove single-entry groups and add them to generalGroup
for key in list(groupedDict.keys()):
    if len(groupedDict[key]) == 1:
        generalGroup.extend(groupedDict.pop(key))

# Optionally, add the generalGroup to the dictionary if it's not empty
if generalGroup:
    groupedDict['generalGroup'] = generalGroup

print(groupedDict)
