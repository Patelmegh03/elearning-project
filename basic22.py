import matplotlib.pyplot as plt
import numpy as np

matches = [1, 2, 3, 4, 5]
dhoni = [7, 45, 73, 20, 21]
kohli = [74, 12, 45, 63, 98]
rohit = [78, 12, 45, 63, 41]

x = np.arange(len(matches))
barwidth = 0.25
plot1 = plt.bar(x - barwidth, rohit, width=barwidth, label="Rohit")
plot2 = plt.bar(x, kohli, width=barwidth, label="Kohli")
plot3 = plt.bar(x + barwidth, dhoni, width=barwidth, label="Dhoni")

plt.bar_label(plot1)
plt.bar_label(plot2)
plt.bar_label(plot3)

plt.xlabel("Matches")
plt.ylabel("Score")
plt.title("Score of the Players")

plt.legend()
plt.show()