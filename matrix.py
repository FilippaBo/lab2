def transpose(matrix):
    if not matrix:  
        return []
    
    rows = len(matrix) 
    cols =len(matrix[0]) 
    new_matrix = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])  
        new_matrix.append(new_row)  

    return new_matrix



def powers(lst,start,end):
    matrix=[]
    for e in range (len(lst)):
        
        new_list=[]
        
        value = float(lst[e])  
        for exponent in range(start,end+1):
            new_value=value**exponent
            new_list.append(new_value)

        matrix.append(new_list)
    return matrix



def matmul(A, B):
    if not A:
        return []
    if not B:
        return []
    
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    C = []

    for i in range(rowsA):
        row = []  
        for j in range(colsB):
            summa = 0  
            for k in range(colsA):
                summa += A[i][k] * B[k][j]

            row.append(summa)
        
        C.append(row)

    return C


def invert(M):
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
   

    A = [[M[1][1] / det, -M[0][1] / det], 
         [-M[1][0] / det, M[0][0] / det]]
    return A


def loadtxt(name):
    x=open(name)
    result=[]
    for line in x.readlines():
        y=line.split()
        tal=[]
        for i in y:
            tal.append(float(i))
        result.append(tal)
    x.close()
    return result
