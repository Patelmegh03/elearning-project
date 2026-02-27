import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f1=pd.read_excel("RESULT1.xls")
f2=pd.read_excel("RESULT2.xls")

alldata=pd.concat([f1,f2])
print(alldata)

name=list(alldata["NAME"])
total=list(alldata["TOTAL"])
plt.bar(name,total)
plt.show()
