# https://www.youtube.com/watch?v=DjYZk8nrXVY youtube link


# explanation -> prefix-sum
# array = [1,2,3,4,5,6,7]
            # i   j
# for example if you are asked to find the sum of sub array items from i tp j 
# we can do for loop but if there are multiple queries there will be O(n*m)
# where m is number of queries and n is the number of arrays
#  we what we can do is first calculate the sum of prefix array from the start to that position

# p[i] = array[0] + array[1] + array[2] + array[3] + + array[i]
# sum from i to j in array will be
# sum[i,j] = p[j] - p[i-1]




# 303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.prefix = [0] * len(nums)
        for i in range(0,len(nums)):
            self.prefix[i] = self.prefix[i-1] + nums[i] if i > 0 else nums[i]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right] if left == 0 else self.prefix[right] - self.prefix[left -1]
        

a = NumArray([-2,0,3,-5,2,-1])
print(a.sumRange(0,2))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)




# pythonic solution
# class NumArray:

#     def __init__(self, nums: list[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left:right+1])






# 525. Contiguous Array
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 
 
 
def find_max_length(arr):
    prefix_sum = 0
    hash_map = {0:-1}
    max_length = 0
    
    for i,num in enumerate(arr):
        prefix_sum += 1 if num > 0 else -1
        
        if prefix_sum in hash_map:
            max_length = max(max_length, i - hash_map[prefix_sum])
        else:
            hash_map[prefix_sum] = i
    return max_length

print(find_max_length([0,1,1,0,0,0,1,0]))




# 560. Subarray Sum Equals K
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.
