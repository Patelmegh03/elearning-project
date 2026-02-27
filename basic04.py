mydata = [{"states":["GUJARAT",
                     "RAJASTHAN",{"PORTION":"WEST INDIA"},
                     {"LANGUAGES":["GUJARATI","MARWADI",
                                   ["HINDI","ENGLISH"]]}]},
            {"CODES":{"GUJARAT":"GJ","RAJASTHAN":"RJ"}},["7.07 CR","8.5 CR"]]
#1
#answer:0

#2
#answer:1

#3
print(mydata[1]["CODES"]["GUJARAT"])

#4
print(mydata[0]["states"][0])

#5
print(mydata[0]["states"][3]["LANGUAGES"][1])

#6
print(mydata[0]["states"][3]["LANGUAGES"][2][1])

#7
print(mydata[0]["states"][2]["PORTION"])

#8
print(mydata[2][0])