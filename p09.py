import pandas as pd

file1=pd.read_excel("RESULT1.xls")
file2=pd.read_excel("RESULT2.xls")
#all name in alphabetical order
alldata=pd.concat([file1,file2])
print(alldata)
print(alldata['NAME'].sort_values())

#merit store in merit.xls
merit=alldata.sort_values(["TOTAL"],ascending=False)
print(merit)
merit.to_excel("marit.xlsx",index=True)

#TOTAL GREATER THAN 200
TOTAL_200=alldata[alldata['TOTAL'] > 200]
print("greater than 200",TOTAL_200)

#LESS THAN 100 AND SAVE IN SHEET
TOTAL_100=alldata[alldata['TOTAL']<100]
print("less than 100",TOTAL_100)
TOTAL_100.to_excel("marit.xlsx",index=True)

#CATEGORY
def categorize(p):
    if p>=80:
        return 'SCHOLER'
    elif p>=50:
        return 'AVERAGE'
    else:
        return 'WEAK'

alldata['CATEGORY'] = alldata['PERCENTAGE'].apply(categorize)

alldata.to_excel('marit.xlsx', index=True)