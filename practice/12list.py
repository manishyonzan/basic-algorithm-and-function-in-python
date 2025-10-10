from collections.abc import Iterable
from collections import Counter
from itertools import groupby

def flatten(lst):
    for each in lst:
        if isinstance(each,Iterable) and not isinstance(each,str):
            yield from flatten(each)
        else:
            yield each
            
            
print(list(flatten([1,2,[1,2],"33"])))
# [1, 2, 1, 2, '33']


# 2 list of indices for specific values
lst = [1,2,3,4,10,2,3,10]
indices = [x for x,y in enumerate(lst) if y ==10]
print(indices)
# [4, 7]

#3 transpose a list of list

matrix = [ [1,2,3],
          [4,5,6],
          [7,8,9]
          ]
transposed = list(map(list,zip(*matrix)))
print(transposed)
# [ [1, 4, 7], 
#  [2, 5, 8], 
#  [3, 6, 9]]



# 4 rotate the elements of list by n positions

def rotate(lst, n):
    return lst[-n:] + lst[:-n]
lst = [1,2,3,4,5]
print(rotate(lst,2))
# [4, 5, 1, 2, 3]


# 5 find the duplicate in the list

lst = [1,2,2,3,4,4,5]

duplicates = [item for item , count in Counter(lst).items() if count > 1]
print(duplicates)
# [2, 4]
#6 chunk a list of n items in each

def chunk(lst,n):
    for i in range(0, len(lst),n):
        yield lst[i:i + n]
        
lst = [1,2,3,4,5,6,7]
chunks = list(chunk(lst,3))
print(chunks)
# [[1, 2, 3], [4, 5, 6], [7]]

#7 remove consecutive duplicates
lst = [1,2,2,3,3,3,4,4,5]
result = [key for key,_ in groupby(lst)]
print(result)

