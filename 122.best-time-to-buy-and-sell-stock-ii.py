from typing import List
#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rets = []
        for i in range(len(prices)-1):
            rets.append(prices[i+1] - prices[i])
        ans = 0
        for ret in rets:
            if ret > 0:
                ans += ret
        return ans
# @lc code=end

