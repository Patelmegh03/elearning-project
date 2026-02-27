import requests

url = requests.get("https://isro.vercel.app/api/spacecrafts")
data = url.json()
print(data)
print(data["spacecrafts"][0]["name"])


