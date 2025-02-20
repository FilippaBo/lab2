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



def polynom_regression(data,n):
    data_transposed = transpose(data)
    #plockar ut data ur fil
    X = data_transposed[0]
    Y = data_transposed[1]


    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]

    Y2=[]
    for x in X: 
        Y2.append(poly(a,x))
    
    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show()


def poly(a,x):
    
    n=len(a)
    for i in a:
        powers(x,0,n)











data=loadtxt("chirps-modified.txt")
polynom_regression(data)

#print(powers([2,3,4],0,2))

