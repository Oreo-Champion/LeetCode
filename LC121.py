# -*- coding: utf-8 -*-


def LC121_MaxProfit3(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0
    p = 0
    cl = prices[0]
    for i in range(1,n):
        cl = min(cl, prices[i])
        p = max(p, prices[i] - cl)
    return p