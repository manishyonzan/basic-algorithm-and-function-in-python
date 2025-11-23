# using naive approach  insertion sort
def getMedian(arr):
    res = []
    res.append(float(arr[0]))
    
    for i in range(1, len(arr)):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
        
        length = i + 1
        
        if length % 2 == 0:
            median = (arr[(length//2) - 1] + arr[length//2]) / 2.0
            print(median, "firrst")
        else:
            median = arr[length//2]
            print(median , "second", i, i//2)
            
        res.append(median)
        
    return res










if __name__ == '__main__':
    arr = [5, 15, 1, 3, 2, 8]
    res = getMedian(arr)
    
    print(" ".join(f"{median:.2f}" for median in res))

            


