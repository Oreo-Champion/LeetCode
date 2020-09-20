from typing import List
#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if i == 0:
                row = [1]
            elif i == 1:
                row = [1, 1]
            else:
                row = [1]
                for j in range(1, i):
                    row.append(ans[-1][j] + ans[-1][j-1])
                row.append(1)
            ans.append(row)
        return ans
# @lc code=end
Solution().generate(5)
