from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt

products = ["Mobile","Laptop","Earbuds","Watch"]
sale = [1200,300,800,600]
plt.bar(products,sale,color = ["Blue","Green","Orange","Red"])
plt.xlabel("PRODUCTS")

plt.ylabel("SALE OF PRODUCT")
plt.title("SALE OF ELECTRICAL ITEM")

plt.show()