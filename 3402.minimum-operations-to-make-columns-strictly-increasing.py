#
# @lc app=leetcode id=3402 lang=python3
#
# [3402] Minimum Operations to Make Columns Strictly Increasing
#

# @lc code=start
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        minimum = 0
        for r in range(rows-1):
            for c in range(cols-1):
                diff = abs(grid[r+1][c] - grid[r][c])
                printf(grid[r+1][c])
                printf(grid[r][c])
                print(diff)
                printf("-------------------------")
                if grid[r+1][c] < grid[r][c]:
                    minimum += diff
                    printf(minimum)

        return minimum




        
# @lc code=end

