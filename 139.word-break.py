from typing import List
#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n+1):
            for w in wordDict:
                tail_match = w == s[i-len(w):i]
                prev_match = dp[i-len(w)]
                if tail_match and prev_match:
                    dp[i] = True
        return dp[-1]
                
            
# @lc code=end
print(Solution().wordBreak('leetcode', ["leet", "code"]))
# Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])
