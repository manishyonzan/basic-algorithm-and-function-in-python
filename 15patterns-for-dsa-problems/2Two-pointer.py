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



