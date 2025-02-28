from numpy import * 
import matplotlib.pyplot as plt
import sys 

def powers(lst,start,end):
    matrix=[]

    for e in range (len(lst)):
        
        new_list=[]
        
        value = float(lst[e])  
        for exponent in range(start,end+1):
            new_value=value**exponent
            new_list.append(new_value)

        matrix.append(new_list)
    
    return array(matrix) 
   


def polynom_regression(data,n):
    data_transposed = transpose(data)
    X = data_transposed[0]
    Y = data_transposed[1]


    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    
        
    sorted_x=sorted(X)
    step=0.2
    num_steps = int((sorted_x[-1] - sorted_x[0]) / step) 
    X2 = linspace(sorted_x[0], sorted_x[-1], num_steps).tolist()

    
    Y2=[]
    for x in X2: 
        Y2.append(poly(a,x))
    
    



    print(Y2)
    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show()


def poly(a,x):
    
    n=len(a)
    function=[]
    for i in range(n):
        r=x**i
        function.append(a[i]*r)
    
    return sum(function)


def main():
    data=loadtxt(sys.argv[1])
    deg=int(sys.argv[2])
    polynom_regression(data,deg)

if __name__ == "__main__":
    main()

