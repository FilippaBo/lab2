def transpose(matrix):
    rows = len(matrix) #=antal rader
    cols =len(matrix[0])#=antal kolonner
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


def matmul(A,B):
    rowsA = len(A) #=antal rader
    rowsB = len(B) #=antal rader
    colsA =len(A[0])#=antal kolonners
    colsB =len(B[0])#=antal kolonner
    print(colsB)
    C = []
    
    for i in range(rowsA):
        for j in range(rowsB):
            step1_A=A[i][j]
            step1_B=B[i][j]
        for k in range(colsA):
            for l in range(colsB):
                step2_A=A[k][l+1]
                step2_B=B[k][l+1]

        square=step1_A*step1_B+step2_A*step2_B
        C.append(square)


    return C  

A = [[0,1]
     ,[1,0]
     ]
B = [[1, 0]
     ,[0,-1]
     ]
print(matmul(A,B))