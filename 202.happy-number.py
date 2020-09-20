#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start


class Solution:
    def isHappy(self, n: int) -> bool:
        cache = []
        while True:
            ans = 0
            for i in list(str(n)):
                int_i = int(i)
                ans += int_i * int_i
            if ans == 1:
                return True
            else:
                if ans in cache:
                    return False
                else:
                    cache.append(ans)
                n = ans
        
# @lc code=end
print(Solution().isHappy(19))
