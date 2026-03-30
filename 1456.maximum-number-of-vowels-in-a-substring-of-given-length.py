#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        start = 0
        end = 0
        maxNumOfVowelLetters = 0
        currentVowels = 0

        for end in range(len(s)):
            if s[end] in vowels:
                currentVowels += 1
            
            if end-start+1 > k:
                if s[start] in vowels:
                    currentVowels -= 1
                start += 1
            
            maxNumOfVowelLetters = max(maxNumOfVowelLetters, currentVowels)

        return maxNumOfVowelLetters
        
# @lc code=end

