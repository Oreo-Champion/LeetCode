import re
#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        num_and_letters = re.findall(r'[a-zA-Z0-9]+', s)
        lower_str = ''.join(num_and_letters).lower()
        return lower_str == lower_str[::-1]
# @lc code=end
Solution().isPalindrome("race a car")
