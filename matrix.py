def transpose(matrix):
    rows = len(matrix) #=antal rader
    cols =len(matrix[0]) #=antal kolonner
    new_matrix = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])  
        new_matrix.append(new_row)  

    return new_matrix

#print(transpose([[1, 2], [3, 4], [5, 6]]))  


def powers(lst,start,end):
    matrix=[]
    for e in range (len(lst)):
        
        new_list=[]
        
        for exponent in range(start,end+1):
            new_value=lst[e]**exponent
            new_list.append(new_value)

        matrix.append(new_list)
    return matrix

#print(powers([2,3,4],0,2))

def matmul(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    C = []

    for i in range(rowsA):
        rad = []  
        for j in range(colsB):
            summa = 0  
            for k in range(colsA):
                summa += A[i][k] * B[k][j]

            rad.append(summa)
        
        C.append(rad)

    return C
#tester matmul:
#A = [[0,1],[1,0]]
#B = [[1, 0],[0,-1]]
#print(matmul(A,B))

#print(matmul([[1, 2, 3], [4, 5, 6]],[[7,8,9,10],[11,12,13,14],[15,16,17,18]]))

#I = [[1,0,0],[0,1,0],[0,0,1]]
#print(matmul(I,[[1, 2, 3], [4, 5, 6],[7, 8, 9]]))


def invert(M):
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    A=[[M[0][1]/det, -M[0][1]/det], [-M[1][0]/det, M[0][0]/det]]
    return A



def loadtxt(name):
    x=open(name)
    result=[]
    for line in x.readlines():
        y=line.split()
        result.append(y)
    x.close()
    return result
#print(loadtxt('chirps.txt'))