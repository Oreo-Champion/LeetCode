
#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for c in s:
            ans *= 26
            ans += ord(c) - (ord('A') - 1)
        return ans
# @lc code=end
Solution().titleToNumber('AA')
