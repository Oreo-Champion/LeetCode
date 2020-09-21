# -*- coding: utf-8 -*-


def LC121_MaxProfit2(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0
    p = [0] * n
    cl = [0] * n
    cl[0] = prices[0]
    for i in range(1,n):
        cl[i] = min(cl[i-1], prices[i])
        p[i] = prices[i] - cl[i]
    return max(p)