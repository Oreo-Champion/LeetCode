from typing import List
#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums)
        nums.reverse()
        nums[:n] = reversed(nums[:n])
        nums[n:] = reversed(nums[n:])
# @lc code=end

Solution().rotate([1,2], 3)
