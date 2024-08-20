# the array need to be sorted first for binary search 
# so the function below is only for sorted array

def binary_search(arr,low:int, high:int,value:int) ->int:
    while (low <= high):
        mid = int(low + (high - low)/2)
        if (arr[mid] == value):
            return mid
        if (arr[mid] < value):
            low = mid + 1
        else:
            high = mid -1
    return -1

array_to_search = [1,2,3,4,5,6,7]
value_to_search = 8
check = binary_search(array_to_search,0,len(array_to_search)-1,value_to_search)

if (check ==-1):
    print("value did not found ")
else:
    print(f"the {value_to_search} is found at position {check + 1}")
    
    
    

