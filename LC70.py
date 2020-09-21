# -*- coding: utf-8 -*-


def LC70_ClimbStairs(n):
    p = 0
    for i in range(n//2 + 1):
        p += comb(n - i, i)
    return p