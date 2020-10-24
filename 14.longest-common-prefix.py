from typing import List
#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
               ans += chars[0] 
            else:
                break
        return ans
# @lc code=end
Solution().longestCommonPrefix(["flower","flow","flight"])
