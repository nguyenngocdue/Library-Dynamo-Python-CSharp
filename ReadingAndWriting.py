'''Read a file'''
from os import write
fil1 = open(r"C:\Users\admin\Desktop\IN.txt","r")
re = fil1.read(5) #read all value in file or read(5) will read the 5 first signs.



'''Write to an Existing File'''
##"a" - Append - will append to the end of the file
fil2 = open(r"C:C:\Users\admin\Desktop\IN.txt","a")
write1 = fil2.write("Now the file has more content!\n")

##"w" - Write - will overwrite any existing content
fil2 = open(r"C:C:\Users\admin\Desktop\IN.txt","w")
write1 = fil2.write("Now the file has more content!\n")

# fil2 = open(r"C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\IronPython.StdLib.2.7.8\os.py","a")
# write1 =fil2.write(str(re))

fil2 = open(r"C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\IronPython.StdLib.2.7.8\os.py","r")
re = fil1.readline() #read all value in file or read(5) will read the 10 first signs.

print(re)
fil1.close()
fil2.close()

'''Create a New File'''
newFil = open(r"C:\Users\admin\Desktop\IN.txt","x")

"""Remove a File or Folder"""
import os
removeFil = os.remove("IN01.txt") 
print(newFil.read())

