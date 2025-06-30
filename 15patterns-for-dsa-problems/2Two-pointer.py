# in two pointer we initializa two variables and move them towards or away each other based on the problem

# two pointer to check the palidrom


def is_palindrome(str):
    start = 0
    end = len(str)-1
    
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return  True

# print(is_palindrome("abcdedcbc"))



# 167. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.
# - Start with one pointer at the beginning (left) and another at the end (right).
# - Check the sum of the two numbers:
# - If it equals the target, return the indices.
# - If it's too large, move the right pointer left.
# - If it's too small, move the left pointer right.
# - Continue until the solution is found.



def twoSum(numbers,target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        if numbers[left] + numbers[right] == target:
            break
        elif numbers[left] + numbers[right] > target:
            right = right - 1
        else:
            left = left + 1 
    return [left+1,right+1]


# print(twoSum([1,2,3,4],3)) 






# leetcode 15 : 3 sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


class Solution():
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        if len(nums) < 3:
            return []
        
        answer = []
        
        for left in range(0,len(nums)):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            
            if nums[left] > 0:
                #no point in searching if the first element is greater than 0 in sorted array to find sum as 0
                break
            
            middle = left + 1
            right = len(nums) - 1
            
            while middle < right:
                total = nums[left] + nums[middle] + nums[right]
                
                if total > 0:
                    right -=1
                elif total < 0:
                    middle += 1
                else:
                    answer.append([nums[left],nums[middle], nums[right]])
                    middle +=1
                    while nums[middle] == nums[middle - 1] and middle < right:
                        middle += 1
        return answer
        
        
                
check = Solution()
print(check.threeSum([-1,0,1,2,-1,-4]))
# def check(x):
#     return tuple(set(x))

# print(check(((1,2,3), (1,2,3))))



# 11 container with most water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        volume = 0
        height_container = 0
        while left < right:
            height_container = height[left] if height[left] < height[right] else height[right]
            
            new_volume = (right - left) * height_container
            
            if new_volume > volume:
                volume = new_volume
            
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1
                