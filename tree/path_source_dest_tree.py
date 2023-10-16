"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
"""
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def lca(node: TreeNode) -> Optional[TreeNode]:
            if not node:
                return None
            if node.val in (startValue, destValue):
                return node # found one of required nodes
            left_val = lca(node.left)
            right_val = lca(node.right)
            if left_val and right_val:
                return node # found lca
            return left_val or right_val # return whatever was found in subtree, could be lca or could be one of the edge nodes, in either case we return the value directly. or between None and a val returns the val
        root = lca(root) # only this subtree is required
        # now do dfs on tree
        stack = [(root, "")] # node, path
        ps, pd = "", ""
        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                ps = path
            if node.val == destValue:
                pd = path
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))
        return "U" * len(ps) + pd
