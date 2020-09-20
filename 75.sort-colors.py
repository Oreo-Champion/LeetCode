from typing import List
#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                if i > j: j = i
            elif nums[j] == 1:
                j += 1
# @lc code=end
Solution().sortColors([2,0,2,1,1,0])
