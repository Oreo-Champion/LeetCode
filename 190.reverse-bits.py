#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int, cache={}) -> int:
        if cache.get(n):
            return cache[n]
        else:
            rev_n = bin(n)[:1:-1]
            fill_n = rev_n + '0' * (32 - len(rev_n))
            ans = int(fill_n, 2)
            cache[n] = ans
            return ans
# @lc code=end
Solution().reverseBits(43261596)
Solution().reverseBits(43261596)