import math
#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        big_num = max(m, n) - 1 # larger number of steps
        small_num = min(m, n) - 1 # smaller number of steps
        order_num = math.factorial(small_num) # number of orders
        ans = 1
        while small_num > 0:
            ans *= big_num + 1
            small_num -= 1
            big_num += 1 
        return int(ans / order_num)
# @lc code=end
Solution().uniquePaths(7, 3)
