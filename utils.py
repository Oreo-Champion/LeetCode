from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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