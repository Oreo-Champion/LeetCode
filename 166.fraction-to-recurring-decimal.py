#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        div, mod = divmod(numerator, denominator)
        if mod == 0: # means div is an integer, like -3.0 -> '3'
            return str(int(div)) 
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator) # get rid of sign
        div, mod = divmod(numerator, denominator)
        ans = ''
        cache_mod = []
        while mod:
            try:
                i = cache_mod.index(mod)
            except ValueError:
                cache_mod.append(mod)
            else:
                break
            if mod < denominator:
                mod *= 10
            div_temp, mod = divmod(mod, denominator)
            ans += str(div_temp)
        else:
            return sign + str(div) + '.' + ans
        return sign + str(div) + '.' + ans[:i] + '(' + ans[i:] + ')'
        
# @lc code=end
print(Solution().fractionToDecimal(7, -12))