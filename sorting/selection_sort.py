def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if (arr[j] < arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


array_to_sort = [1,4,5,6,3]    
sorted_array  = selection_sort(array_to_sort)
print(sorted_array)
