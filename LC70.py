class Solution:
    def climbStairs(self, n: int) -> int:
        step_1, step_2, count = n, 0, 0
        while step_1>=0:
            count += math.comb(step_1+step_2,step_1)
            step_1 -= 2
            step_2 += 1
        return count