mydata= {
"maharashtra":{"mumbai":{"city":"metro city","metro":"yes"}, "population":"20 cr"},
"gujarat": ["AHMEDABAD","SURAT","RAJKOT"],
"rajasthan":["AJMER","JAISALMER",{"capital":"jaipur"},["MEWAD","RJ","INR"]]
}

#A
print(mydata.keys())

#B
print(len(mydata))

#1
print(mydata["maharashtra"]["mumbai"]["city"])

#2
print(mydata["rajasthan"][2]["capital"])

#3
print(mydata["gujarat"][2])

#4
print(mydata["rajasthan"][3][1])