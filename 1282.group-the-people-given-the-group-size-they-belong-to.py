#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        result = []
        hashtable = {}

        for i, num in enumerate(groupSizes):

            if num not in hashtable:
                hashtable[num] = []
            hashtable[num].append(i)
            
            if len(hashtable[num]) == num: 
                result.append(hashtable[num])
                hashtable[num] = []

        return result



        
# @lc code=end

