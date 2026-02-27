import numpy as np

#2*6 array and flatten
a26=np.random.randint(0,50,(2,6))
print("2*6 array",a26)
print("flatten array",a26.flatten())

#create 5d array
a5d=np.random.randint(12,56,(2,2,2,2,2))
print(a5d)

#searsh about 100d and 10d array

#create random matrix and add[1,2,3]
matrix=np.random.randint(0,9,(2,3))
print("matrix\n",matrix)
add=np.array([1,2,3])
print("add [1,2,3]:\n",matrix+add)