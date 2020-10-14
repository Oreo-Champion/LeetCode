import collections
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def create_list(arr: List):
    p = head = ListNode(arr[0])
    for i in range(1, len(arr)):
        p.next = ListNode(arr[i])
        p = p.next
    return head

def show_list(head: ListNode):
    while head:
        print(head.val)
        head = head.next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(arr: List):
    if len(arr) == 0: return None
    dummy = TreeNode()
    queue = collections.deque([(dummy, -1)])
    flag_map = {-1: 'left', 1: 'right'}
    for i in range(0, len(arr)):
        node, flag = queue.popleft()
        if arr[i] is not None:
            new_node = TreeNode(arr[i])
            setattr(node, flag_map[flag], new_node)
            queue.extend([(new_node, -1), (new_node, 1)])
    return dummy.left


def bfs_tree(root: TreeNode) -> List:
    queue = collections.deque([root])
    ans = []
    while queue:
        node = queue.popleft()
        if node is not None:
            ans.append(node.val)
            queue.extend([node.left, node.right])
    return ans

def show_tree(root: TreeNode, order='bfs') -> None:
    assert order in {'bfs', 'nlr', 'lnr', 'lrn'}
    func_map = {'bfs': bfs_tree}
    print(func_map[order](root))
    
        
if __name__ == "__main__":
    show_tree(create_tree([1, None, 2, 3]))