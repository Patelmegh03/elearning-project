import xlrd

file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

i=1
for i in range (1,sheet.ncols):
        print(sheet.cell_value(0,i),",",end=" ")


