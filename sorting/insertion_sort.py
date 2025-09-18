# pseudo code
# 1 work from left to right
# 2 examine each item and compare its item to left
# insert the item into correct position  in its array


def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j = j-1
    return arr
        
arr2  = insertion_sort([2,3,7,1,16])
print(arr2)