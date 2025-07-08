# Read an Excel file by first converting it to CSV,
# then reading the CSV using Python's built-in csv module
import pandas as pd
import csv
import os

def read_excel_and_return_data(xlsx_path):
    if not os.path.exists(xlsx_path):
        raise FileNotFoundError(f"File not found: {xlsx_path}")
    # Convert Excel to a temporary CSV file
    temp_csv = os.path.splitext(xlsx_path)[0] + "_temp.csv"
    df = pd.read_excel(xlsx_path, sheet_name=0)
    df.to_csv(temp_csv, index=False, encoding='utf-8-sig')

    # Read the newly created CSV
    data = []
    with open(temp_csv, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    # Delete the temporary CSV file (optional)
    os.remove(temp_csv)

    return data
# Call the function
path = r"A:\TRAINING DYNAMO API\PART 47 READ EXCEL\ReadExcel.xlsx"
data = read_excel_and_return_data(path)

# Print the result
for row in data:
    print(row)
# If using this in Dynamo, assign to OUT
OUT = data


# Read an Excel file using pandas
import pandas as pd
# Path to the Excel file
file_path = r"A:\TRAINING DYNAMO API\PART 47 READ EXCEL\ReadExcel.xlsx"
# Read the entire sheet without treating any row as header
df = pd.read_excel(file_path, engine='openpyxl', header=None)
# Loop through each row and store it in a list
rows = []
for index, row in df.iterrows():
    row_data = row.tolist()  # convert each row (Series) to a list
    rows.append(row_data)
# Print the result
for r in rows:
    print(r)
# If needed, store the result
OUT = rows
