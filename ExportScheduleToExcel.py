import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

schedule_list = IN[0]
path = IN[1]
fileName_list = IN[2]

result_list = []
for index, sched, in enumerate(schedule_list):
    schedule = UnwrapElement(sched)
    fileName = fileName_list[index]
    try:
        export_options = ViewScheduleExportOptions()
        schedule.Export(path, fileName, export_options)
        result_list.append("Schedule Exported ")
    except:
        result_list.append("Export Failure")
OUT = result_list