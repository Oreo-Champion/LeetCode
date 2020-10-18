import itertools
import collections
from typing import List
#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    
    def is_valid(self, arr: List[str]) -> bool:
        cntr = collections.Counter(arr)
        cntr['.'] = 0
        if cntr.most_common(1)[0][1] > 1:
            return False
        else:
            return True

    def get_cols(self, board: List[List[str]]):
        for j in range(len(board[0])):
            col = []
            for i in range(len(board)):
                col.append(board[i][j])
            yield col

    def get_boxes(self, board: List[List[str]]):
        blocks = (range(0, 3), range(3, 6), range(6, 9))
        for rows, cols in itertools.product(blocks, blocks):
            box = []
            for i in rows:
                for j in cols:
                    box.append(board[i][j])
            yield box
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid(row): return False
        for col in self.get_cols(board):
            if not self.is_valid(col): return False
        for box in self.get_boxes(board):
            if not self.is_valid(box): return False
        return True
# @lc code=end
inp = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(inp))
