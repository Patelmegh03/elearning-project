import xlrd

file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

ui=input("Enter Name of cricketer:")
f=False
for i in range (1,sheet.ncols):

    if sheet.cell_value(0,i) == ui:
        print(f"Cricketer name found at row:0 and column:{i} ")
        break
else:
    print("Name not found")