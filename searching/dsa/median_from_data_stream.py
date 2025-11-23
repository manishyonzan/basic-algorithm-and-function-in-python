def getMedian(arr):
    res = []
    res.append(float(arr[0]))
    
    for i in range(1, len(arr)):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
        
        print(i)
        if i % 2 == 0:
            median = (arr[(i//2) - 1] + arr[i//2]) / 2.0
            print(median, "firrst")
        else:
            median = arr[i//2]
            print(median , "second")
            
        res.append(median)
        
    return res

if __name__ == '__main__':
    arr = [5, 15, 1, 3, 2, 8]
    res = getMedian(arr)
    
    print(" ".join(f"{median:.2f}" for median in res))

            
