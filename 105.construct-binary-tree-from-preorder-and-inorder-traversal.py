from typing import List
#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if inorder:
    #         root_val = preorder.pop(0)
    #         idx = inorder.index(root_val)
    #         root = TreeNode(root_val)
    #         root.left = self.buildTree(preorder, inorder[:idx])
    #         root.right = self.buildTree(preorder, inorder[idx+1:])
    #         return root
    #     return None
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder.pop(0)
        idx = inorder.index(val)
        root = TreeNode(val)
        stack = [
            (root, 'left', preorder[:idx], inorder[:idx]),
            (root, 'right', preorder[idx:], inorder[idx+1:])]
        while stack:
            node, direction, preorder, inorder = stack.pop(0)
            if not preorder:
                continue
            val = preorder.pop(0)
            idx = inorder.index(val)
            setattr(node, direction, TreeNode(val))
            stack.extend([
                (getattr(node, direction), 'left', preorder[:idx], inorder[:idx]),
                (getattr(node, direction), 'right', preorder[idx:], inorder[idx+1:])])
        return root


# @lc code=end
Solution().buildTree([1, 2, 4, 5, 3, 6, 7, 9, 8], [4, 2, 5, 1, 3, 7, 9, 6, 8])
