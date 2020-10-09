#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        turtle = rabbit = head
        while True:
            try:
                turtle = turtle.next
                rabbit = rabbit.next.next
            except AttributeError:
                return False
            if turtle is rabbit:
                return True
            if turtle is head:
                return False
            
# @lc code=end

