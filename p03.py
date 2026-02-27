import pandas as pd

#file handling
file = "mydata.xls"
fp = pd.read_excel(file)
print(fp)
print(fp["KOHLI"])