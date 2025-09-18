# given a matrix an (array of arrays) rotate the matrix 90 degrees and return it for instance
"""

1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

"""
# reverse the list without using [::-1]

# lst = [1, 2, 3, 4, 5]
# reversed_lst = []
# for i in lst:
#     reversed_lst = [i] + reversed_lst
# print(reversed_lst) 

"""
1,2,3,4,5

5,4,3,2,1
"""

# transpose of a matrix

# for column in range(number_of_col):
#         temp = []
#         for row in range(number_of_row):
#             temp.append(matrix[row][column])
#         new_matrix.append(temp)

"""

1 2 3
4 5 6
7 8 9

1 4 7
2 5 8
3 6 9

"""

# solution would be to transpose the matrix and then reverse the element position in the row

def rotate(matrix):
    number_of_row = len(matrix)
    number_of_col = len(matrix[0])
    new_matrix =[]
    
    # transpose of matrix in new matrix
    for column in range(number_of_col):
        temp = []
        for row in range(number_of_row):
            temp.append(matrix[row][column])
        new_matrix.append(temp)
        
    # reverse the element of each row
    for index,row in enumerate(new_matrix):
        temp =[]
        for element in row:
            temp = [element] + temp
        new_matrix[index] = temp
    return new_matrix
    


print(rotate([[1,2,3],[4,5,6], [7,8,9]]))
        
    
    
