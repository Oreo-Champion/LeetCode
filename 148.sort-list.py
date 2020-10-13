from utils import *
import types
#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.


class Solution:
    
    # def sortList(self, head: ListNode) -> ListNode:
    #     if head is None: return head
    #     def iter_func(self):
    #         self.now = self
    #         return self

    #     def next_func(self):
    #         if self.now is not None:
    #             ans = self.now
    #             self.now = self.now.next
    #             return ans
    #         else:
    #             raise StopIteration

    #     setattr(ListNode, '__iter__', iter_func)
    #     setattr(ListNode, '__next__', next_func)
    #     p = ans = ListNode()
    #     for node in sorted(head, key=lambda node: node.val):
    #         p.next = node
    #         p = p.next
    #     p.next = None
    #     return ans.next

    def split(self, cur, size):
        if cur is None: return None, None
        head, n = cur, 0
        while True:
            if cur is None:
                return head, None
            if n+1 == size:
                cur.next, cur = None, cur.next
                return head, cur
            cur = cur.next
            n += 1

    def merge(self, tail, l, r):
        p, q = l, r
        while p or q:
            if p is None:
                tail.next, q = q, q.next
            elif q is None:
                tail.next, p = p, p.next
            else:
                if p.val <= q.val:
                    tail.next, p = p, p.next
                else:
                    tail.next, q = q, q.next
            tail = tail.next
        return tail

    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        n, cur = 0, head
        while cur is not None:
            cur = cur.next
            n += 1

        size = 1
        dummy, dummy.next = ListNode(), head
        l, r, tail = None, None, dummy
        while size < n:
            cur, tail = dummy.next, dummy
            while cur:
                l, cur = self.split(cur, size)
                r, cur = self.split(cur, size)
                tail = self.merge(tail, l, r)
            size <<= 1
        return dummy.next


# @lc code=end
show_list_node(Solution().sortList(create_list_node([-1, 5, 3, 4, 0])))
