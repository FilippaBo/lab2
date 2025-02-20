from numpy import * #stjärnan =hämtar hela doc
import matplotlib.pyplot as plt


def powers(lst,start,end):
    matrix=[]

    for e in range (len(lst)):
        
        new_list=[]
        
        value = float(lst[e])  #gör om till int. vet inte om det är rätt men det slutade komma error
        for exponent in range(start,end+1):
            new_value=value**exponent
            new_list.append(new_value)

        #x=array(new_list)
        matrix.append(new_list)
    
    #list_of_list=array(matrix)
    return array(matrix) 
    #return list_of_list
   # return x 



data=loadtxt("chirps-modified.txt")
data_transposed = transpose(data)
#plockar ut data ur fil
X = data_transposed[0]
Y = data_transposed[1]


Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
print(b,m)
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

print(powers([2,3,4],0,2))

