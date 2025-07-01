# 643 Maximum Average Subarray I
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        max_sum = sum(nums[:k])
        print(max_sum)
        check = max_sum

        #  for i in range(k, len(nums)): you can also do this
        for i in range(n - k):
            check = check - nums[i] + nums[k + i]
            print(check)
            if check > max_sum:
                max_sum = check
                
        
        print(max_sum)   
        return max_sum / float(k)
    
    
a = Solution()
b = a.findMaxAverage([1,12,-5,-6,50,3],4)
print(b)
