from utils import *
#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head, odd_tail, even_head, even_tail = [None] * 4
        p, i = head, 0
        while p:
            i += 1
            if i == 1:
                odd_head = odd_tail = p
            elif i == 2:
                even_head = even_tail = p
            elif i % 2 != 0:
                odd_tail.next = p
                odd_tail = p
            elif i % 2 == 0:
                even_tail.next = p
                even_tail = p
            p = p.next
        if i % 2 == 0 and odd_tail is not None:
            odd_tail.next = None
        elif i % 2 != 0 and even_tail is not None:
            even_tail.next = None
        if odd_tail is not None:
            odd_tail.next = even_head
        return odd_head


# @lc code=end
show_list_node(Solution().oddEvenList(create_list_node([1, 2, 3, 4, 5])))
