import requests
url = requests.get("https://api.mfapi.in/mf")
data= url.json()

print(len(data))

#scheme code:12345 Scheme name:xyz
for i in range(0,len(data)):
    print("schemecode:",data[i]["schemeCode"],"schemeName:",data[i]["schemeName"])