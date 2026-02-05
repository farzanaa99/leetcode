#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        maxArea = 0

        while start < end:
            if height[end] < height[start]:
                area = height[end] * (end-start)
                end-=1
            else: 
                area = height[start] * (end-start)
                start+=1

            if area > maxArea:
                maxArea = area
        
        return maxArea


# @lc code=end

