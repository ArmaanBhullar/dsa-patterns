"""
https://leetcode.com/problems/invert-binary-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert_tree(node: Optional[TreeNode]) -> TreeNode:
            if node is None:
                return None
            else:
                inverted_left = invert_tree(node.left)
                inverted_right = invert_tree(node.right)
                node.right = inverted_left
                node.left = inverted_right
                return node
        return invert_tree(root)