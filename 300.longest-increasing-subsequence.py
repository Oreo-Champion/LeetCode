from typing import List
import bisect
#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start

class Solution:
    
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n <= 1: return n
    #     dp = [1] * n
    #     max_ans = 1
    #     for i in range(1, n):
    #         max_val = 0
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 max_val = max(max_val, dp[j])
    #         dp[i] = max_val + 1
    #         max_ans = max(max_ans, dp[i])
    #     return max_ans

    def lengthOfLIS(self, nums: List[int]) -> int:
        a = []
        for num in nums:
            i = bisect.bisect_left(a, num)
            if i == len(a):
                a.append(num)
            else:
                a[i] = num
        return len(a)

# @lc code=end
# Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])