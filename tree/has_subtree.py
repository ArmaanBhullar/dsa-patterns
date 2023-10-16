"""
https://leetcode.com/problems/subtree-of-another-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BestSolution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.root = root
        self.sub_root = subRoot
        self.merkle(self.root)
        self.merkle(self.sub_root)
        return self.check_tree(self.root)

    def check_tree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.m == self.sub_root.m:
            return True
        else:
            return self.check_tree(root.left) or self.check_tree(root.right)

    def merkle(self, root: Optional[TreeNode]) -> str:
        # adds hash of tree to the node
        if root is None:
            return '#' # no need to assign anything here
        else:
            hash_val = hash(f"{root.val}, {self.merkle(root.left)}, {self.merkle(root.right)}")
            root.m = hash_val
            return hash_val

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.sub_root = self.serialize(subRoot)
        self.is_same = False
        temp = self.serialize_with_check(root)
        return self.is_same or (temp == self.sub_root)

    def serialize_with_check(self, node: Optional[TreeNode]) -> Tuple:
        if node is None:
            return 'x'
        left_tree = self.serialize_with_check(node.left)
        right_tree = self.serialize_with_check(node.right)
        self.is_same = self.is_same or (left_tree == self.sub_root)
        self.is_same = self.is_same or (right_tree == self.sub_root)
        return node.val, left_tree, right_tree

    def serialize(self, node: Optional[TreeNode]) -> Tuple:
        if node is None:
            return 'x'
        else:
            return node.val, self.serialize(node.left), self.serialize(node.right)