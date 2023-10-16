"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.candidates = []
        self.k = k
        self.found = False
        self.in_order(root)
        return max(self.candidates)

    def in_order(self, node: Optional[TreeNode]) -> int:
        if node is not None:
            self.in_order(node.left)
            if len(self.candidates) < self.k:
                self.candidates.append(node.val)
            else:
                return None
            self.in_order(node.right)