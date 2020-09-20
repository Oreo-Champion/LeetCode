from typing import List
#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, digit in enumerate(digits[::-1]):
            num += digit * 10 ** i
        num += 1
        return [int(digit) for digit in list(str(num))]
# @lc code=end
Solution().plusOne([1,2,3])
