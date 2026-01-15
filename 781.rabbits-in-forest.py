#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        hashtable = {}
        min = 0

        for i, num in enumerate(answers):
            if num not in hashtable or hashtable[num] == 0:
                min += num + 1 
                hashtable[num] = num

            else: 
                hashtable[num] -= 1 

        return min

        
# @lc code=end

