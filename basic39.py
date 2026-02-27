import numpy as np

aa=np.array([10,20,30])
bb=np.array([[1],[2],[3]])

print(aa,"\n",bb)
print("Sum of aa and bb\n",aa+bb)
print("Subtraction of aa and bb\n",aa-bb)
print("Multiplaction of aa and bb\n",aa*bb)
print("Div of aa and bb\n",aa/bb)
print("Power of aa\n",aa**2)
print("Sum of aa",np.sum(aa))

#create 4*4 array
cc=np.random.randint(0,100,(4,4))
print("4*4 array\n",cc)

#create 1d array 0 to 20 in five stape
print("1d array 1 to 20 in 5 stape",np.linspace(0,20,5))

#find row and column
x=np.array([[5,10,15],[8,7,9]])
print("last row",x[1])
print("second column",x[:,1])
print("middle element",x[1,1])

#row wise and column wise
r2d= np.array([[1, 2, 3],[4, 5, 6]])

print("Row wise sum",np.sum(r2d,1))
print("Column wise sum",np.sum(r2d,0))