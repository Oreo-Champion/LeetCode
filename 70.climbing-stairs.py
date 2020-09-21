#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
import math
import collections

# @lc code=start


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     div, mod = divmod(n, 2)
    #     ans = 0
    #     while div >= 0:
    #         A_sum = math.factorial(div + mod)
    #         A_div = math.factorial(div)
    #         A_mod = math.factorial(mod)
    #         add = A_sum / (A_div * A_mod)
    #         ans += int(add)
    #         div -= 1
    #         mod += 2
    #     return ans
    
    # def climbStairs(self, n: int) -> int:
    #     p = 0
    #     for i in range(n//2 + 1):
    #         p += math.comb(n - i, i)
    #     return p
    
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     else:
    #         return self.climbStairs(n-1) + self.climbStairs(n-2)
        
    # def climbStairs(self, n: int) -> int:
    #     q = collections.deque([n])
    #     ans = 0
    #     while q:
    #         n = q.popleft()
    #         if n == 1:
    #             ans += 1
    #         elif n == 2:
    #             ans += 2
    #         else:
    #             q.extend([n-1, n-2])
    #     return ans
    
    def climbStairs(self, n: int) -> int:
        ans = [1, 1] + [0] * (n-1)
        for i in range(2, n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[-1]

# @lc code=end
assert Solution().climbStairs(35) == 14930352
# print(Solution().climbStairs(2))
