from typing import List
#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return sum(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = max(nums[i] + ans[i-2], ans[i-1])
        return ans[-1]
# @lc code=end

