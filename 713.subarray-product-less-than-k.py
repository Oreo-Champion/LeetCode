from typing import List

#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        head, tail = 0, 0 
        n = len(nums)
        prod = 1
        count = 0
        while tail < n:
            prod *= nums[tail]
            while prod >= k and tail >= head:
                prod /= nums[head]
                head += 1
            tail += 1
            count += tail - head
        return count


# @lc code=end
# print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0))
# print(Solution().numSubarrayProductLessThanK(
#     [10, 3, 3, 7, 2, 9, 7, 4, 7, 2, 8, 6, 5, 1, 5], 30))
