#public
def getDataRowOfSchedule(schedule):
    table = obj.GetTableData().GetSectionData(SectionType.Body)
    nRows = table.NumberOfRows
    nColumns = table.NumberOfColumns
    #Collect all of data from the schedule
    dataListRow = []
    for row in range(nRows): #Iterate through the rows. The second row is always a blank space
        dataListColumn = []
        for column in range(nColumns): #Iterate through the columns
            dataListColumn.Add( TableView.GetCellText(obj, SectionType.Body, row, column) )
        dataListRow.Add( dataListColumn );
    return dataListRow
#public
def getSchedulableFields(schedule):
    return schedule.Definition.GetSchedulableFields()
#public
def addColumnToSchedule(schedule, column_name):
    # Get the existing fields
    schedule_fields = schedule.Definition.GetSchedulableFields()
    # Find the SchedulableField by name
    emptyField = []
    for field in schedule_fields:
        if field.GetName(doc) == column_name:
            schedulable_field = field
            try:
                TransactionManager.Instance.EnsureInTransaction(doc)
                schedule.Definition.AddField(schedulable_field)
                TransactionManager.Instance.TransactionTaskDone()
            except:
                emptyField.append(column_name)
    return "'" +  ', '.join(emptyField) + "'" + 'fields is included in Schedule'