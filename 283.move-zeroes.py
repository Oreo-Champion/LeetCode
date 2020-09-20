from typing import List
#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                j -= 1
            else:
                i += 1
# @lc code=end
Solution().moveZeroes([0,0,1])

