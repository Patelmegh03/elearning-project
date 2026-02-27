import numpy as np
mylistv = [1,2,3,4,5,6,7,8]
arr = np.array(mylistv)
print(arr)

a =np.array([10,20,30,40])
print(a)
print(type(a))

b = np.array([[1,2,3],[4,5,6]])
print(b)

c = np.zeros
print(c)

d = np.ones
print(d)

e = np.linspace(10,100,20)
print(e)

aa = np.array([10,20,30])
bb = np.array([[1],[2],[3]])
print(aa)
print(bb)
print(aa+bb)

x = np.arange(12)
print(x)

res = x.reshape(3,4)
print(res)

y = res.flatten()
print(y)

l = np.random.randint(0,100,(2,2))
print(l)
m = np.random.randint(2,30,(2,3,4))
print(m)
n = np.random.randint(0,1000,(3,4,5,6,7))
print(n)