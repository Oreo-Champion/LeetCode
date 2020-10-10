from utils import create_list_node, show_list_node
#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p, n = head, 0
        while p:
            n += 1
            p = p.next
        p, rev, i = head, None, 0
        while p:
            i += 1
            if i > n // 2:
                rev, rev.next, p = p, rev, p.next
            else:
                p = p.next
        p = head
        while rev and p:
            if rev.val != p.val:
                return False
            else:
                rev, p = rev.next, p.next 
        return True
# @lc code=end
# Solution().isPalindrome(create_list_node([1,2,3,2,1]))
Solution().isPalindrome(create_list_node([1,2,2,1]))