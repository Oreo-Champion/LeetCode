from typing import List
#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count >= 2:
            return [0] * len(nums)
        elif zero_count == 1:
            prod = 1
            for num in nums:
                prod = prod * num if num != 0 else prod * 1
            return [0 if num!=0 else prod for num in nums]
        else:
            prod = 1
            for num in nums:
                prod = prod * num
            return [int(prod / nums[i]) for i in range(len(nums))]
# @lc code=end
print(Solution().productExceptSelf([1, 0]))
