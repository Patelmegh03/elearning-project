import xlrd

file = ("MY DATA.xlsx")
openbook =  xlrd.open_workbook(file)
sheet = openbook.sheet_by_index(0)

rohit_score = []

for i in range(1, sheet.nrows):
    rohit_score.append(int(sheet.cell_value(i, 1)))

sum = sum(rohit_score)
ans = sum / 7
print("Average score of Rohit", ans)