import xlrd

file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

kohli_score = []

for i in range (1,sheet.nrows):
    kohli_score.append(int(sheet.cell_value(i,2)))

maximum=max(kohli_score)
print("Maximum runs scored by kohli:",maximum)