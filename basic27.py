import xlrd

file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

ds=[]

for i in range (1,sheet.nrows):

    ds.append(int(sheet.cell_value(i, 3)))

sum=sum(ds)
print("Total runs of Dhoni:",sum)