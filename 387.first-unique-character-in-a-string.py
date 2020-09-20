from collections import Counter
#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_cntr = Counter(s)
        for i, car in enumerate(s):
            if s_cntr[car] == 1:
                return i
        return -1
# @lc code=end
Solution().firstUniqChar("dddccdbba")