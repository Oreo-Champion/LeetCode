from typing import List
#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, temp_sum = nums[0], 0
        for num in nums:
            temp_sum = max(num, num+temp_sum)
            max_sum = max(max_sum, temp_sum)
        return max_sum
    
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        ret = []
        for i in range(len(prices) - 1):
            ret.append(prices[i+1] - prices[i])
        return max(0, self.maxSubArray(ret))

# @lc code=end

print(Solution().maxProfit([2,1,2,1,0,1,2]))