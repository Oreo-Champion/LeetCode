from typing import List, Tuple
import copy
#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start


class Solution:

    def find_surr(self, i: int, j: int, m: int, n: int) -> List[Tuple]:
        """
        Find surrounding cells
        """
        surr = [(p, q) for p in (i, i + 1, i - 1) for q in (j, j + 1, j - 1)
                if not (p == i and q == j) and 0 <= p < m and 0 <= q < n]
        return surr

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # 2: dies -> live, -1: live -> dies
        for i in range(m):
            for j in range(n):
                count = 0
                for p, q in self.find_surr(i, j, m, n):
                    count = count + 1 if board[p][q] == 1 or board[p][q] == -1 else count
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -1
        # Change 2 back to 1; -1 back to 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

# @lc code=end


Solution().gameOfLife([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
])
