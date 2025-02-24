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



def polynom_regression(data,n,step):
    data_transposed = transpose(data)
    #plockar ut data ur fil
    X = data_transposed[0]
    Y = data_transposed[1]


    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()
    #print(Xp)
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    
        
    sorted_x=sorted(X)

    """To construct X2 start with the smallest number in X and finish with the biggest.
      You can choose n by dividing the difference between the smallest and the biggest 
      number by a small step. In our experiments step 0.2 works well.    
      - menar de att n=0.2 eller att vi väljer n och ett annat värde step=0.2?
      - ska det vara så här och blir då num_steps = n och behöver vi skicka in n?"""
    
    num_steps = int((sorted_x[-1] - sorted_x[0]) / step) 
    X2 = linspace(sorted_x[0], sorted_x[-1], num_steps).tolist()

    
    Y2=[]
    for x in X2: 
        Y2.append(poly(a,x))
    
    



    print(Y2)
    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show()


def poly(a,x):
    
    n=len(a)
    function=[]
    for i in range(n):
        #r=powers(x,0,n) 
        r=x**i
        function.append(a[i]*r)
    
    return sum(function)

#print(poly([1,2,3],4))

data=loadtxt("chirps-modified.txt")
polynom_regression(data,2,0.2)

#print(powers([2,3,4],0,2))


