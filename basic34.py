import xlrd
import matplotlib.pyplot as plt
import numpy as np

file=("MY DATA.xlsx")
openbook=xlrd.open_workbook(file)
sheet=openbook.sheet_by_index(0)
rs=[]
ks=[]
ds=[]


for i in range (1,sheet.nrows):

    rs.append(int(sheet.cell_value(i, 1)))
    ks.append(int(sheet.cell_value(i, 2)))
    ds.append(int(sheet.cell_value(i, 3)))


m=[1,2,3,4,5,6,7]
x=np.arange(len(m))+1
b=0.15
p1=plt.bar(x-0.15,rs,width=b,label="ROHIT",color="Blue")
p2=plt.bar(x,ks,width=b,label="KOHLI",color="Orange")
p3=plt.bar(x+0.15,ds,width=b,label="DHONI",color="Green")
plt.bar_label(p1,rs)
plt.bar_label(p2,ks)
plt.bar_label(p3,ds)
plt.xlabel("Match")
plt.ylabel("Scores")
plt.title("Score of the player")
plt.legend()
plt.show()