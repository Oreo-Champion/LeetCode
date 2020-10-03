#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        if strx[0] == '-':
            ans = -int(strx[:0:-1])
        else:
            ans = int(strx[::-1])
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        else:
            return ans
# @lc code=end
Solution().reverse(-123)
