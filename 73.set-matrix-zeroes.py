from typing import List
#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def markCol(self, matrix: List[List[int]], j, marker='0') -> None:
        """
        Mark Jth Col's non-zero value to marker
        """
        for i in range(len(matrix)):
            if matrix[i][j] != 0:
                matrix[i][j] = marker
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        marker = '0'
        for i in range(m):
            any_zero = False
            for j in range(n):
                if matrix[i][j] == 0:
                    any_zero = True
                    self.markCol(matrix, j, marker)
            if any_zero:
                matrix[i] = [0] * n
        # change marker to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == marker:
                    matrix[i][j] = 0
                
                    
# @lc code=end

Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])