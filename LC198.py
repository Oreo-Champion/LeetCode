# -*- coding: utf-8 -*-


def LC198_Rob(self, nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [nums[0], max(nums[0:2])]
    c = 2
    while c < n:
        dp.append(max(dp[-1], dp[-2] + nums[c]))
        c += 1
    return dp[-1]