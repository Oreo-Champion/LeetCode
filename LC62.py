# -*- coding: utf-8 -*-


def LC62_UniquePaths(nums: List[int]) -> int:
    return comb(m+n-2, n-1)