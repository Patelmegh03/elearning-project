import xlrd

file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)


for i in range (1,sheet.nrows):
    print(f"Match {i} Runs:")
    print(f"Score of Rohit:{sheet.cell_value(i,1)}")
    print(f"Score of Kohli:{sheet.cell_value(i,2)}")
    print(f"Score of Dhoni:{sheet.cell_value(i,3)}")