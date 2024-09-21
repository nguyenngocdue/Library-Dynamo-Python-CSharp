myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for key, value in myfamily.items():
    for val in value.values():
        print(val)


numbers = { x:{"X": x, "Y": x+10, "Z": x+20} for x in range(100)}
print(numbers)