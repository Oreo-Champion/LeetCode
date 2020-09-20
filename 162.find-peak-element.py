from typing import List
#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        head, tail = 0, len(nums) - 1
        while head < tail:
            mid = (head + tail) // 2
            if nums[mid] > nums[mid + 1]:
                tail = mid
            else:
                head = mid + 1
        return head

# @lc code=end
Solution().findPeakElement([1,2,3,1])
