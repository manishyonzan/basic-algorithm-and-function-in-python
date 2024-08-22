def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n-1):
            if (arr[i] < arr[j]):
                min_index
            