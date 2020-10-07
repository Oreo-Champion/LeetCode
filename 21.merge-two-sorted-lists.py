#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p0 = l0 = ListNode()
        p1, p2 = l1, l2
        while p1 or p2:
            if p1 and p2:
                if p1.val <= p2.val:
                    val = p1.val
                    p1 = p1.next
                else:
                    val = p2.val
                    p2 = p2.next
            elif p1:
                val = p1.val
                p1 = p1.next
            else:
                val = p2.val
                p2 = p2.next
            p0.next = ListNode(val)
            p0 = p0.next
        return l0.next
        
# @lc code=end

