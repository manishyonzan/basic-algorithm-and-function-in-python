def merge_sort(arr):
    if (len(arr)<=1):
        return arr
    
    mid = int(len(arr)/2)
    left_half = arr[:mid]
    right_half = arr[mid:]
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return merge(sorted_left,sorted_right)

def merge(left,right):
    result = []
    while (len(left) and len(right) > 0):
        if (left[0] > right[0]):
            result.append(right[0])
            del right[0]
        else:
            result.append(left[0])
            del left[0]
    while (len(left) > 0):
        result.append(left[0])
        del left[0]
    while (len(right) > 0):
        result.append(right[0])
        del right[0]
        
    # i can replace two while loop of above using below code
    #    result.extend(left)
    #    result.extend(right)
    
    return result


array_to_sort = [1,2,3,4,5,8,7,9,9,8]
sorted_array = merge_sort(array_to_sort)

print(sorted_array)     
    