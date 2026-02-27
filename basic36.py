import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
average_temperature = [5, 7, 10, 15, 20, 25, 30, 28, 22, 18, 12, 6]

plt.scatter(months, average_temperature, color='Red',alpha = 1,)
plt.title("Average Monthly Temperature")
plt.xlabel("Months", fontweight='bold')
plt.ylabel("Temperature", fontweight='bold')
plt.xticks(rotation=45)
plt.show()