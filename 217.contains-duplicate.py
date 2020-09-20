from typing import List
import collections
#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        cntr = collections.Counter(nums)
        return cntr.most_common(1)[0][1] > 1
# @lc code=end
Solution().containsDuplicate([1,2,3,1])
