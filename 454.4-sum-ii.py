import collections
from typing import List
#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AplusB = collections.Counter([a + b for a in A for b in B])
        return sum(AplusB[-c-d] for c in C for d in D)
# @lc code=end

Solution().fourSumCount([1,2], [-2,-1], [-1,2], [0,2])
