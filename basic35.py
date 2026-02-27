import matplotlib.pyplot as plt
import numpy as np

sales_product_a=[150,200,250,300]
sales_product_b=[180,220,210,260]
sales_product_c=[140,190,230,280]

m=["Q1","Q2","Q3","Q4"]
x=np.arange(len(m))+1
b=0.15
p1=plt.bar(x-0.15,sales_product_a,width=b,label="product_a",color="Blue")
p2=plt.bar(x,sales_product_b,width=b,label="products_b",color="Red")
p3=plt.bar(x+0.15,sales_product_c,width=b,label="products_c",color="Yellow")
plt.bar_label(p1,sales_product_a)
plt.bar_label(p2,sales_product_b)
plt.bar_label(p3,sales_product_a)
plt.xlabel("Products",fontweight = 'bold')
plt.ylabel("Price",fontweight = 'bold')
plt.title("Graph of products")
plt.legend()
plt.show()