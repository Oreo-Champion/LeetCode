import collections
from typing import List
#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in cache:
                cache[sorted_string] = [string]
            else:
                cache[sorted_string].append(string)
        return cache.values()
# @lc code=end


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
