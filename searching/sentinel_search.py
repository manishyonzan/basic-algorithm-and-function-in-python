def sentinel_search(arr,length_of_array,value):
    last = arr[length_of_array-1]
    if (last == value):
        return length_of_array - 1
    index = 0
    arr[length_of_array-1] = value
    while (arr[index] != value):
        index +=1
    if (index<(length_of_array-1)):
        return index
    else:
        return -1
    
array_to_search = [1,2,3,4,9,10]
value_to_search = 9

return_value = sentinel_search(array_to_search,len(array_to_search),value_to_search)

if (return_value ==-1):
    print("Value did not found")
else:
    print(f"value found at array index {return_value}")
    
        