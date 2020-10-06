from typing import List
#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     p, q = head, None
    #     while p:
    #         q = ListNode(p.val, q)
    #         p = p.next
    #     return q

    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(head, None)
        
    def helper(self, p: ListNode, q: ListNode) -> ListNode:
        if p is None:
            return q
        else:
            q = ListNode(p.val, q)
            return self.helper(p.next, q)
        
# @lc code=end

def create_list_node(arr: List):
    p = head = ListNode(arr[0])
    for i in range(1, len(arr)):
        p.next = ListNode(arr[i])
        p = p.next
    return head

def show_list_node(head: ListNode):
    while head:
        print(head.val)
        head = head.next

# head = create_list_node([1,2,3,4,5])
# show_list_node(head)

show_list_node(Solution().reverseList(create_list_node([1,2,3,4,5])))
