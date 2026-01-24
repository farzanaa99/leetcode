#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)

        for i in range(1, len(s), 2):
            prev_char = s[i - 1]
            shift_amount = int(s[i])

            s[i] = chr(ord(prev_char) + shift_amount)

        return "".join(s)

# @lc code=end

