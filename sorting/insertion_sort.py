def insertion_sort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        for j in range(0,i+1):
            if (arr[j]<arr[i]):
                return