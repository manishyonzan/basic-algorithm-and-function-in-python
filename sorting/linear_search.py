def linear_search(arr, targetValue):
    for i in range(0,len(arr)):
        if targetValue == arr[i]:
            return i
    return -1

print(linear_search([1,2,3,4,5], 6))
    