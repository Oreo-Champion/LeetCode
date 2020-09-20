from typing import List
#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sort_nums = sorted(nums, reverse=True)
        n = len(sort_nums)
        mid = n // 2
        for i in range(mid):
            nums[2*i+1] = sort_nums[i]
        for i in range(mid, n):
            nums[2*(i-mid)] = sort_nums[i]
# @lc code=end
Solution().wiggleSort([1,5,1,1,6,4])
