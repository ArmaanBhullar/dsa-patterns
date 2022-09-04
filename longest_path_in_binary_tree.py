from typing import Optional
# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node: TreeNode) -> int:
            # return length of the longest path to a leaf node from node

            if node == None:
                return 0

            left_longest = dfs(node.left)
            right_longest = dfs(node.right)

            self.diameter = max(self.diameter, left_longest + right_longest + 1)

            return 1 + max(left_longest, right_longest)

        dfs(root)

        return self.diameter - 1
