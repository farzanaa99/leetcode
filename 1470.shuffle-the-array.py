#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        start = 0
        mid = n
        result = []
        left = True

        while start < n or mid < len(nums):
            if left:
                result.append(nums[start])
                start+=1
            else: 
                result.append(nums[mid])
                mid+=1
            left = not left
        return result

        
        

# @lc code=end

