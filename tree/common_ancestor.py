"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # maintain a left and right flag which tell is p or q is in left or right subtree of a node, first hit where left and right is True is returned
        self.ans = None
        self.p = p.val
        self.q = q.val
        self.dfs(root)
        return TreeNode(self.ans)

    def dfs(self, node: Optional[TreeNode]) -> bool:

        # base case
        if node is None:
            return False
        # print(node.val)
        # print(node.val)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # print(left, right)
        if left and right:
            self.ans = node.val
        elif left or right:
            # print(node.val, left, right)
            if (node.val == self.p) or (node.val == self.q):
                self.ans = node.val
        if (node.val == self.p) or (node.val == self.q):
            # print(node.val, True)
            return True
        else:
            # print(node.val, False)
            return left or right or False