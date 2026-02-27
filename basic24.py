import xlrd

file = ("MY DATA.xlsx")
openbook = xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

# Display some basic info
print(sheet)
print(sheet.cell_value(0, 0))
print(sheet.cell_value(5, 2))
print("The number of rows:", sheet.nrows)
print("The number of columns:", sheet.ncols)

print("\nAll rows")
for i in range(sheet.nrows):
    print(sheet.row(i))

print("\nAll cols")
for k in range(sheet.ncols):
    for m in range(sheet.nrows):
        print(sheet.cell_value(m, k))

try:
    userinput = float(input("\nEnter your score: "))
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    exit()

found = False
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        if sheet.cell_value(i, j) == userinput:
            print("\n Score is found!")
            print(f" The data is at row {i + 1} and column {j + 1}")
            found = True
            break
    if found:
        break

if not found:
    print("\n Score is not found.")


