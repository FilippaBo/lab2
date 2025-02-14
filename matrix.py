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

print(transpose([[1, 2], [3, 4], [5, 6]]))  
