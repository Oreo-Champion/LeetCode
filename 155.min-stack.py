import collections
#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = collections.deque()
        self._min = collections.deque([1e10])
        
    def push(self, x: int) -> None:
        self._stack.append(x)
        self._min.append(min(x, self._min[-1]))

    def pop(self) -> None:
        item = self._stack.pop()
        self._min.pop()
        return item

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

