# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        cache = []
        forward_p = ('(', '[', '{')
        backward_p = (')', ']', '}')
        p_map = {f: b for f, b in zip(forward_p, backward_p)}
        for car in s:
            if car in forward_p:
                cache.append(car)
            else:
                if cache:
                    remove = cache.pop()
                    if car != p_map[remove]:
                        return False
                else:
                    return False
        return False if cache else True
                
# @lc code=end

Solution().isValid('[')