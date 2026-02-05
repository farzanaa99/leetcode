#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return (start+1, end+1)
            elif numbers[start] + numbers[end] < target:
                start+=1
            else:
                end-=1
        
        return -1
        
# @lc code=end

