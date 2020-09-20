from typing import List
import itertools
#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            for item in itertools.combinations(nums, i + 1):
                ans.append(list(item))
        return ans
# @lc code=end
print(Solution().subsets([1,2,3]))
