"""
https://leetcode.com/problems/same-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same_tree(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if (left is None) and (right is None):
                return True
            elif left is None or right is None:
                return False
            else:
                return (left.val == right.val) and (is_same_tree(left.left, right.left) and (is_same_tree(left.right, right.right)))
        return is_same_tree(p, q)