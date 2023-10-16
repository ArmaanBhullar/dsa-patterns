"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.recursive_parse(preorder, inorder)

    def recursive_parse(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(preorder) == 0:
            return None
        # print(preorder)
        root_val = preorder[0]
        root_index = inorder.index(root_val) # works because unique
        return TreeNode(val= root_val,
        right = self.recursive_parse(preorder[root_index+1:], inorder[root_index+1:]),
        left = self.recursive_parse(preorder[1:root_index+1], inorder[:root_index]))