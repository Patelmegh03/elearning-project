

import requests

url = requests.get(f'https://api.postalpincode.in/pincode/382350')
data= url.json()
print(data)
print(data[0]["PostOffice"][0]["Name"])

for i in range(0,len(data[0]["PostOffice"])):
   print(data[0]["PostOffice"][i]["Name"])

if data[0]["Status"] == "Success":
    for i in range(0, len(data[0]["PostOffice"])):
        print(data[0]["PostOffice"][i]["Name"])

else:
    print("Invalid Pincode")