#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if root is None: return True
        stack = [(root.left, root.right)]
        while stack:
            p, q = stack.pop()
            if p is None and q is None: continue
            elif p is None or q is None or p.val != q.val: return False
            stack.append((p.left, q.right))
            stack.append((p.right, q.left))
        return True
    
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is None: return True
    #     return self.helper(root.left, root.right)

    # def helper(self, p: TreeNode, q: TreeNode) -> bool:
    #     if p is None and q is None: return True
    #     elif p is None or q is None: return False
    #     return p.val == q.val and self.helper(p.left, q.right) and self.helper(p.right, q.left)

# @lc code=end
