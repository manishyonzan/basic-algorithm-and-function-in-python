
# the matrix needs to be sorted

def searchMatrix(matrix, key):
    n = len(matrix)
    m = len(matrix[0])
    
    s = 0
    e = n * m - 1
    
    while (s<=e):
        mid = s + (e - s)//2
        row_index = mid//m
        col_index = mid % m
        
        if(matrix[row_index][col_index] == key):
            return True
        elif (key < matrix[row_index][col_index]):
            e = mid - 1
        else:
            s = mid +1
    return False


print(searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]], 24))        