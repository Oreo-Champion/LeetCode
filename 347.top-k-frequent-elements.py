import collections
from typing import List
#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i, f in collections.Counter(nums).most_common(k)]
# @lc code=end

