import math
#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start


class Solution:
    def numSquares(self, n: int) -> int:
        LARGE_INT = 10**10
        if n <= 0:
            return 0
        counter = [0] + [LARGE_INT] * n
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                counter[i] = min(
                    counter[i], counter[i-j*j]+1)
                j += 1
        return counter[-1]

    # def numSquares(self, n: int) -> int:
    #     # Lagrange's four-square theorem
    #     if int(math.sqrt(n))**2 == n:
    #         return 1
        
    #     for j in range(int(math.sqrt(n)) + 1):
    #         if int(math.sqrt(n - j*j))**2 == n - j*j:
    #             return 2

    #     while n % 4 == 0:
    #         n >>= 2
    #     if n % 8 == 7:
    #         return 4
        
    #     return 3


# @lc code=end
Solution().numSquares(12)
