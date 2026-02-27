import xlrd



file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

v1 = int(sheet.cell_value(2, 1))
v2 = int(sheet.cell_value(5, 3))
v3 = sheet.cell_value(0, 3)
v4 = int(sheet.cell_value(4, 2))
v5 = int(sheet.cell_value(7, 3))

print(f"{v1},{v2},{v3},{v4},{v5}")