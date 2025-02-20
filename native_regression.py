from matrix import * #stjärnan =hämtar hela doc
import matplotlib.pyplot as plt

data=loadtxt("chirps.txt")
data_transposed = transpose(data)
#plockar ut data ur fil
X = data_transposed[0]
Y = data_transposed[1]


Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
m=float(m)
b=float(b)

#temperature=25
#predicted_number_of_chirps = b + m * temperature   
#print(predicted_number_of_chirps,b,m)

Y2=[]
for i in X: 
    Y2.append(b + m * i) 

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()

