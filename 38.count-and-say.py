import itertools
#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:

    def say(self, s: str) -> str:
        return ''.join([str(len(list(g))) + str(k) for k, g in itertools.groupby(s)])
                       
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.say(self.countAndSay(n-1))
# @lc code=end

print(Solution().countAndSay(5))
