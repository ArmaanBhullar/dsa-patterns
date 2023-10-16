#https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # maintain a defaultdict of list, do a dfs, append node to it's level which is the key in the dict
        from collections import defaultdict
        if not root:
            return []
        self.levels = defaultdict(list)
        self.dfs(root, 0)
        ls = []

        max_level = max(self.levels.keys())
        for i in range(max_level + 1):
            ls.append(self.levels[i])
        return ls

    def new(self) -> str:
        return "u"

    def dfs(self, node: Optional[TreeNode], level: int) -> None:
        if node is not None:
            self.levels[level].append(node.val)
            self.dfs(node.left, level + 1)
            self.dfs(node.right, level + 1)
        else:
            pass
