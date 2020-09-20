from typing import List
#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        prev_num = nums[0]
        i, j = 1, len(nums)
        while i < j:
            if nums[i] == prev_num:
                nums.pop(i)
                j -= 1
            else:
                prev_num = nums[i]
                i += 1
        return len(nums)
        
# @lc code=end
Solution().removeDuplicates([1,2,2])
