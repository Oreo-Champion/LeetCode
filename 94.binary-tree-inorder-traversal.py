import collections
from typing import List
from utils import create_tree
#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root is None:
    #         return []
    #     else:
    #         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack = collections.deque([root])
    #     ans = []
    #     while stack:
    #         item = stack.pop()
    #         if item is None:
    #             continue
    #         elif isinstance(item, int):
    #             ans.append(item)
    #         else:
    #             stack.extend([item.right, item.val, item.left])
    #     return ans

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Morris Traversal
        # Step 1: Initialize current as root
        # Step 2: While current is not NULL,
        # If current does not have left child
        #     a. Add current’s value
        #     b. Go to the right, i.e., current = current.right
        # Else
        #     a. In current's left subtree, make current the right child of the rightmost node
        #     b. Go to this left child, i.e., current = current.left

        ans = []
        while root:
            if root.left is None:
                ans.append(root.val)
                root = root.right
            else:
                cur = left = root.left
                while cur.right:
                    cur = cur.right
                cur.right = root
                root.left = None
                root = left
        return ans


# @lc code=end
print(Solution().inorderTraversal(create_tree([3, 1, None, None, 2])))
