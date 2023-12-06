import os

path_to_check = r'C:\Users\NGUYEN NGOC DUE\AppData\Roaming\Dynamo\Dynamo Revit\2.10\packages\packages\BIM3DM\lib'
import sys
sys.path.append(path_to_check)
import BIM3DM
import getpass
username = getpass.getuser()
OUT =  username

