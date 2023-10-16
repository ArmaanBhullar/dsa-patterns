"""
https://leetcode.com/problems/validate-binary-search-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # find max of left and min of right and compare with root recursively
        self.is_valid = True
        self.is_valid_bst(root)
        return self.is_valid

    def is_valid_bst(self, root: Optional[TreeNode]) -> Tuple[int]:
        # returns min and max for left and right respectively, while checking condition along the way
        if root is None:
            return float('+inf'), float('-inf')
        min_left, max_left = self.is_valid_bst(root.left)
        min_right, max_right = self.is_valid_bst(root.right)
        if root.val <= max_left or root.val >= min_right:
            self.is_valid = False
        return min(root.val, min_left, min_right), max(root.val, max_left, max_right)
