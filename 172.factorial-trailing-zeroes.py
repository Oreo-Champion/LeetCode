#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        num_power = 1
        num_div = n // 5 ** num_power
        while num_div >= 1:
            ans += num_div
            num_power += 1
            num_div = n // 5 ** num_power
        return ans
# @lc code=end
print(Solution().trailingZeroes(125))
