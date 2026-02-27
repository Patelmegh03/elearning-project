import matplotlib.pyplot as plt

day = ["Monday","Tuseday","Wednesday","Thursday","Friday"]
temp = [45,46,44,41,43]
plt.plot(day,temp,color = "Red",linestyle = '-',marker = 'o',label = "Ahemdabad")
temp = [43,42,47,45,43]
plt.plot(day,temp,color = "Blue",linestyle = '--',marker = '^',label = "Mehsana")
temp = [44,48,49,46,47]
plt.plot(day,temp,color = "Green",linestyle = ':',marker = '*',label = "Surat")
plt.title("Temp graph")
plt.xlabel('Days')
plt.ylabel("Temprature")
plt.legend()
plt.show()








