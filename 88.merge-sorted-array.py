from typing import List
#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                m += 1
            i += 1
        if j == n:
            nums1[m:] = []
        else:
            nums1[i:] = nums2[j:]


# @lc code=end
# Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# Solution().merge([0], 0, [1], 3)
# Solution().merge([2, 0],
#                  1,
#                  [1],
#                  1)
Solution().merge([4, 5, 6, 0, 0, 0],
                 3,
                 [1, 2, 3],
                 3)
