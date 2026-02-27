mydata= {"category":[{"A":"FIRST","package":{"data":"2lacs"}},
{"B":"Second","data":{"new":[100]}},{"C":"Third","Tests":[45,75,25]}]};

#A
print(mydata.keys())

#B
print(len(mydata))

#1
print(mydata["category"][0]["package"]["data"])

#2
print(mydata["category"][2]["Tests"][2])

#3
print(mydata["category"][1]["data"]["new"][0])