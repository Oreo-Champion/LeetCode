from typing import List
#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        temp_chars = []
        prev = None
        chars.append(chr(127))
        while chars:
            char = chars.pop(0)
            if prev is not None and char != prev:
                ans.append(temp_chars[0])
                if len(temp_chars) > 1:
                    ans.extend(list(str(len(temp_chars))))
                temp_chars.clear()
            temp_chars.append(char)
            prev = char
        chars.extend(ans)
        return len(chars)


# @lc code=end
print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
