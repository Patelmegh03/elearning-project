import requests
import matplotlib.pyplot as plt

url = "https://randomuser.me/api/?results=50"
response = requests.get(url)
data = response.json()

ages = [user['dob']['age'] for user in data['results']]

plt.hist(ages, bins=5, color='skyblue', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age Groups", fontweight='bold')
plt.ylabel("Number of Users", fontweight='bold')
plt.show()