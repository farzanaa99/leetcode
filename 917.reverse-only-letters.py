#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        st = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            if st[start].isalpha() and st[end].isalpha():
                st[start] = s[end]
                st[end] = s[start]
                start += 1
                end -= 1
            elif not st[start].isalpha():
                start += 1
            else:
                end -= 1

        return "".join(st)

        
# @lc code=end

