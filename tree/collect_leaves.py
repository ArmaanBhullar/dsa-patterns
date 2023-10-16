"""
https://leetcode.com/problems/find-leaves-of-binary-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # traverse while storing the height of a node from it's children

        self.depth_dict = defaultdict(list)

        def post_order(node: TreeNode) -> None:
            if node is not None:
                left_height = post_order(node.left)
                right_height = post_order(node.right)
                height = max(left_height, right_height) + 1
                self.depth_dict[height].append(node.val)
                return height
            else:
                return 0

        post_order(root)

        # print(self.depth_dict)
        max_depth = max(self.depth_dict.keys())
        ls = []
        for i in range(1, max_depth + 1):
            ls.append(self.depth_dict[i])
        return ls