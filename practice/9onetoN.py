# given a array and number return all the array that is not in the serial increasing array

def returnNotinarray(arr:list,N:int):
    """
    params:
    (
        arr: list of array that is to be checked for 
        N: to check until this array
    )
     returns:
     array of number that is not in the arr array from 1 to N
    
    """
    arr.sort()
    arr = set(arr)
    return [x for x in range(1,N+1) if x not in arr]
    
    
    return arr

arr = [1,2,3,5,4,34,6,6]
N = 25
print(returnNotinarray(arr,N))