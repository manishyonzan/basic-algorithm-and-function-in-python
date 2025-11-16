def binary_search(sorted_arr, targetValue):
    left = 0
    right = len(sorted_arr) -1
    steps = 0
    
    while left<= right:
        mid = (left + right)//2
        
        if  sorted_arr[mid] == targetValue:
            return mid
        if sorted_arr[mid] < targetValue:
            left = mid + 1
        else:
            right = mid - 1
            
        steps+=1
        print("it  is step no", steps)
    return -1

print("checking the binary search steps", binary_search([1,2,3,4,5,6,7,8,9], 4))
            