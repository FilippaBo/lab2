from matrix import * 
import matplotlib.pyplot as plt

data=loadtxt("chirps-modified.txt")
data_transposed = transpose(data)
X = data_transposed[0]
Y = data_transposed[1]


Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
print(b,m)
m=float(m)

b=float(b)


Y2=[]
for i in X: 
    Y2.append(b + m * i) 

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()

