from typing import List
import collections
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = collections.Counter(nums)
        return cntr.most_common(1)[0][0]
# @lc code=end

