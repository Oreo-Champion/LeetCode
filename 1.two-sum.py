#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in nums_map:
                return [nums_map[left], i]
            else:
                nums_map[nums[i]] = i
                
# @lc code=end

