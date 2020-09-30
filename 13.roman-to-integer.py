#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
    ROMAN_DIGIT_MAP = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000}

    def romanToInt(self, s: str) -> int:
        i, ans = 0, 0
        while i < len(s):
            if i < len(s) - 1 and (
                (s[i] == 'I' and s[i+1] in {'V', 'X'})
                or (s[i] == 'X' and s[i+1] in {'L', 'C'})
                or (s[i] == 'C' and s[i+1] in {'D', 'M'})
            ):
                ans += self.ROMAN_DIGIT_MAP[s[i+1]] - self.ROMAN_DIGIT_MAP[s[i]]
                i += 2
                continue
            ans += self.ROMAN_DIGIT_MAP[s[i]]
            i += 1
        return ans


# @lc code=end
print(Solution().romanToInt("IV"))
