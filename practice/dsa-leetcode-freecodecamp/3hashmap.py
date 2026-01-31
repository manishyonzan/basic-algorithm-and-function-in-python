# how does hashfunction store data: for a key it will calculate number that is available in memory 
# and points to it and the value is save in that memory so hash function is faster or 0(1) in insert and lookup it itself has the memory location
# the key must be hashable , in general numbers, strings, tuples are hashable not the array, dictionary because its content change and the hash function needs same value



# frequency map

my_map = {}

data = [1,2,3,4,5,3,6,9,11,9,2]
for item in data:
    if item not in my_map:
        my_map[item] = 1
    else:
        my_map[item] +=1
        
print(my_map)




# question
# given a array of integers and an integer target return the indexes of two number whose sum is equal to the target integer


def two_sum(arr:list[int], target_value:int)-> list[int]:
    num_to_index = {}  
    for index, num in enumerate(arr):
        complement = target_value - num
        if complement in num_to_index:
            return [index,num_to_index[complement]]
        else:
            num_to_index[num] = index
    return []