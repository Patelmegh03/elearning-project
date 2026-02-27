import matplotlib.pyplot as plt
brand = ["Gucci","Louboutin","Louis vuitton","Dior","Versace"]
share = [30,15,25,20,10]
plt.pie(share,labels=brand,autopct="%1.1f%%",colors=["Coral","Yellow","Crimson","Red","Pink"])
plt.title("Share hold of company")

plt.show()