#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        is_prime = [True] * n
        for i in range(2, n):
            if not is_prime[i]:
                continue
            j = i
            while j * i <= n - 1:
                is_prime[i * j] = False
                j += 1
        return sum(is_prime) - 2
# @lc code=end
Solution().countPrimes(10)
