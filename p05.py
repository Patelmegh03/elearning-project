import requests
import pandas as pd
from pandas import json_normalize


url = requests.get("https://isro.vercel.app/api/spacecrafts")
data=url.json()

data1=pd.json_normalize(data["spacecrafts"])
print(data1)


