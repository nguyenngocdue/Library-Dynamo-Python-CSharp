import clr
clr.AddReference("System")  
import System

from pyrevit import forms, script
import os
from System.Windows import Application, Window
from System.Windows.Forms import Application, Button, Form, Label, TextBox, CheckBox, FolderBrowserDialog, OpenFileDialog, DialogResult, ComboBox, FormBorderStyle

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

import bim3dm as BIM3DM

#-------------------------------------------------------------------

def get_path_file():
    fileDialog = System.Windows.Forms.OpenFileDialog()
    fileDialog.ShowDialog()
    return fileDialog.FileName
def get_path_directory():
    fileDialog = FolderBrowserDialog()
    fileDialog.ShowDialog()
    return fileDialog.SelectedPath
def create_get_directory(parent_dir, directory):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    # print("Directory '% s' created" % directory)
    return path
def create_file(file_name, folder_path):
    file_path = folder_path + '\\' +  file_name
    f = open(file_path, "a")
    f.close()
    return file_path

def write_file(file_path, content, typeWrite):
    f = open(file_path, typeWrite)
    f.write(content)
    f.close()
    return file_path
def path_leaf(path):
    import ntpath
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def copy_paste_file(srcFile, targetFile):
    import shutil
    shutil.copy2(srcFile, targetFile)
def getFoldersInFolder(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return folders
def getNames(names):
    return [os.path.splitext(i)[0] for i in names]
def refreshBundle(bundle_path, values):
    with open(bundlePath, "w") as f:
        f.write("layout:" + "\n")
        f.close()
    for name in toolNamesCurrent:
        f = open(bundlePath, 'a')
        f.write("- " + name + "\n")
        f.close()



parent_dir  = r"C:\Users\NGUYEN NGOC DUE\AppData\Roaming\pyRevit-Master\extensions\pyBIM3DM.extension\pyBIM3DM.tab"

#Create a tool name
folders = getFoldersInFolder(parent_dir)
toolNamesCurrent = getNames(folders)


bundlePath = parent_dir + "\\" + "bundle.yaml"
refreshBundle(bundlePath,toolNamesCurrent)


# ask for file
with forms.WarningBar(title='Data Entry Form'):
    dataForm = BIM3DM.ask_DynamoScript()

source_fileDyn = dataForm['txtb_dyn_path']
source_fileIcon = dataForm['txtb_icon_path']
panel_name = dataForm['txtPanel_name']
button_name = dataForm['txtTool_name']


# Create directories
directory_panel = panel_name + ".panel"
panel_path = create_get_directory(parent_dir, directory_panel)
directory_pushbutton = button_name + ".pushbutton"
pushbutton_path = create_get_directory(panel_path , directory_pushbutton)


if(source_fileDyn == ''):
    # create 2 files ("script.py", "bundle.yaml")
    files_name = ["script.py", "bundle.yaml"]
    for file in files_name:
        file_path = create_file(file, pushbutton_path)
        write_file(file_path,  "print('BIM3DM Hello Everyone')", "w")
        
        targetIcon = pushbutton_path + "\\" + "icon.png"
        copy_paste_file(source_fileIcon,targetIcon)

        bundle_name =  "- " + panel_name + "\n"
        write_file(bundlePath, bundle_name, "a")

else:
    if not button_name and not source_fileDyn:
        forms.alert("You must enter [Name + Script's path]  to use this tool.", exitscript=True)

    file_name_extension = path_leaf(source_fileDyn)
    file_name = os.path.splitext(file_name_extension)[0]
    new_file_name_extension = file_name + "_script" + ".dyn"

    # paste file .dyn + icon
    targetFile = pushbutton_path + "\\" + new_file_name_extension
    targetIcon = pushbutton_path + "\\" + "icon.png"
    copy_paste_file(source_fileIcon,targetIcon)
    copy_paste_file(source_fileDyn, targetFile)

    # create 2 files ("script.py", "bundle.yaml")
    files_name = ["script.py", "bundle.yaml"]
    for file in files_name:
        file_path = create_file(file, pushbutton_path)
        content = "Tooltip: " + file_name + "\n" + "Author : pyBIM3DM"
        write_file(file_path, content, "w")
    bundle_name =  "- " + panel_name + "\n"
    write_file(bundlePath, bundle_name, "a")


# reload all tools
res = True
if res:
    from pyrevit.loader import sessionmgr
    sessionmgr.reload_pyrevit()
