class Solution:
    def find_closest_to_zero(nums:list):
        closest = nums[0]
        
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
     
# Time: O(n)
# Space: O(1)
 