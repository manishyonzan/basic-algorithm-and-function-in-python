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



# 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        
        longest_substring = 1
        substring = s[0]
        print("\n")
        for i in range(1, len(s)):
            print(s[i])
            if s[i] in substring:
                substring = substring[substring.index(s[i]) + 1:] + s[i]
            else:
                substring = substring + s[i]
            if len(substring) > longest_substring:
                longest_substring = len(substring)
                
        return longest_substring
            
            
        

a = Solution()
m = a.lengthOfLongestSubstring("abcdabc")
print(m)
