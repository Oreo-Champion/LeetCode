from typing import List
#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, temp_sum = nums[0], 0
        for num in nums:
            temp_sum = max(num, num+temp_sum)
            max_sum = max(max_sum, temp_sum)
        return max_sum
# @lc code=end
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
