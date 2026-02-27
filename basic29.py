import xlrd



file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

for i in range (0,sheet.nrows):
        print(sheet.cell_value(i,3),",",end=" ")