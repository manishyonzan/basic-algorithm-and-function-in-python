def linear_Search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return 1
    return -1

list_of_values = [1,2,3,4,5]


while True:
    try:
        x = int(input("Whats x?"))
        result = linear_Search(list_of_values,x)
        if result ==1:
            print("Value is in the array.")
        else:
            print("value is not in the array.")
        
    except ValueError:
        print("x is not a number")
    else:
        break
    


