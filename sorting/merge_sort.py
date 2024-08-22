def merge_sort(arr):
    if (len(arr)<=1):
        return arr
    
    mid = len(arr)/2
    left_half = arr[:mid]
    right_half = arr[mid:]
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return 

def merge(left,right):
    result = []
    i = j = 0
    
    