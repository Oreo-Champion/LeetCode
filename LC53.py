# -*- coding: utf-8 -*-


def LC53_MaxSubArray(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return sum(nums)
    p = nums[0]
    mp = p
    for i in range(1, n):
        p = max(nums[i], p + nums[i])
        mp = max(mp, p)
    return mp