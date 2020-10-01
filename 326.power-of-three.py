import math
#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        logv = math.log(n, 3)
        return abs(logv - round(logv)) < 1e-10
# @lc code=end
Solution().isPowerOfThree(243)
