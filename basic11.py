import requests

url = requests.get("http://universities.hipolabs.com/search?country=india")
data= url.json()

#PRINT NAME OF ALL universities.

#1
for i in range(0,len(data)):
    print("name:",data[i]["name"])

#2
for i in range(0,5):
    print("Name:", data[i]["name"], "| Country:", data[i]["country"])

#3

print("Total:", len(data))

#4

for i in range(len(data)):
    if "Delhi" in data[i]["name"]:
        print("Name:", data[i]["name"], "| Website:", data[i]["web_pages"][0])

#5

for i in range(0,len(data)):
    if data[i]["name"].startswith("Indian"):
        print("Name:", data[i]["name"])

#6

website_list = []
simple_wesite_list = []

for i in range(0,len(data)):
    print("website : " , data[i]["web_pages"])
    website_list.extend(data[i]["web_pages"])
    simple_wesite_list.append(data[i]["web_pages"])

print("Web site with extend variable",website_list)
print("Web site with append variable",simple_wesite_list)


#7

for i in range(0,len(data)):
    print("Name:", data[i]["name"], "| Alpha to Code:", data[i]["alpha_two_code"])

#8

for i in range(0,len(data)):
    if len(data[i]["web_pages"]) > 1:
        print("Name : " , data[i]["name"])


#9

longest_name = ""
for i in range(0,len(data)):
    if len(data[i]["name"]) > len(longest_name):
        longest_name = data[i]["name"]
print("longest Name : ",longest_name)


#10

for i in range(len(data)):
    if "Technology" in data[i]["name"]:
        print("Name:", data[i]["name"])