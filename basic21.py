import matplotlib.pyplot as plt

stock_price=[900,800,950,700,500,650,400,500,550,200,250,100,230,400,570,1000,920,450,540,780]
plt.hist(stock_price,bins = 4,color = "Black", edgecolor = "White")
plt.show()