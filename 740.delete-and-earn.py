from typing import List
import collections
#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cntr = collections.Counter(nums)
        using, avoid = 0, 0
        prev = None
        for i in sorted(cntr):
            if i - 1 != prev:
                avoid, using = max(using, avoid), cntr[i] * i + max(using, avoid)
            else:
                avoid, using = max(using, avoid), cntr[i] * i + avoid
            prev = i
        return max(using, avoid)
            

# @lc code=end
print(Solution().deleteAndEarn([1,2,2,3,3,3,4,4,4,4]))
