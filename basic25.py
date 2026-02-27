import openpyxl

# Load workbook and active sheet
file = "MY DATA.xlsx"
wb = openpyxl.load_workbook(file)
sheet = wb.active

# Initialize score lists
rohit_score = []
kohli_score = []
dhoni_score = []

# Read data from second row onward
for row in sheet.iter_rows(min_row=2, max_col=4, values_only=True):
    rohit_score.append(int(row[1]))   # 2nd column (index 1)
    kohli_score.append(int(row[2]))   # 3rd column (index 2)
    dhoni_score.append(int(row[3]))   # 4th column (index 3)

print(rohit_score)
