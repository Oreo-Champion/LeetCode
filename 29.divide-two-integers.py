#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if dividend * divisor > 0 else -1
        div, _ = divmod(abs(dividend), abs(divisor))
        if div > 2**31 - 1 and sign == 1: div = 2**31 - 1
        elif div > 2**31 and sign == -1: div = 2**31
        return -div if sign == - 1 else div
# @lc code=end

