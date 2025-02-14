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

print(powers([2,3,4],0,2))




#def matmul(A,B):
