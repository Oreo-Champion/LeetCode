#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     pA, pB = headA, headB
    #     cache = set()
    #     while pA:
    #         cache.add(id(pA))
    #         pA = pA.next
    #     while pB:
    #         if id(pB) in cache:
    #             return pB
    #         pB = pB.next
    #     return None
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        if pA is None or pB is None: return None
        while pA is not pB:
            if pA.next is not None:
                pA = pA.next
            else:
                endA = pA.val
                pA = headB
            if pB.next is not None:
                pB = pB.next
            else:
                endB = pB.val
                pB = headA
            if 'endA' in locals().keys() and 'endB' in locals().keys() and endA != endB:
                return None
        return pA
# @lc code=end

