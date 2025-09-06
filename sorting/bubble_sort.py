# how it works in each iteration highest goes to the right / lowest goes to the left depends how it is implemented
# 1,8,7,6
# 1,7,6,8
# 1,6,7,8




def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
                
    return arr

arrayto = [1,6,5,7,8,9,11,2]

a = bubble_sort(arrayto)

print(a)
