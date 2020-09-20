from typing import List
from collections import Counter
#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cntr1, cntr2 = Counter(nums1), Counter(nums2)
        ans = []
        for elem in cntr1:
            count = min(cntr1[elem], cntr2[elem])
            ans.extend([elem]*count)
        return ans
# @lc code=end

Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])