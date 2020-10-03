from typing import List
#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = l0 = ListNode()
        div = 0 # carry
        while True:
            div, l0.val = divmod(div + l1.val + l2.val, 10)
            l1, l2 = l1.next, l2.next
            if l1 or l2 or div > 0:
                l1 = ListNode() if not l1 else l1
                l2 = ListNode() if not l2 else l2
                l0.next = ListNode()
                l0 = l0.next
            else:
                break
        return root
            
# @lc code=end

