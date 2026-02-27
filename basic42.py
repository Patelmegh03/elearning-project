#multi indexing
import pandas as pd

index = pd.MultiIndex.from_tuples([("CSE",2022),("CSE",2023),
                                  ("ECE",2022),("ECE",2023)],
                                  names=["Department","Year"])

data = [78,97,36,78]
df = pd.DataFrame(data,index=index,columns=["pass %"])
print(df)