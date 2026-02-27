import requests

url = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
data = url.json()
print(data)

print(len(data.keys()))

print(data.keys())

print(data["market_data"]["current_price"]["usd"])