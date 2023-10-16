# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/829015001/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        self.max_at_each_node(root)
        return self.global_max

    def max_at_each_node(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_max = max(self.max_at_each_node(node.left), 0)
        right_max = max(self.max_at_each_node(node.right), 0)
        # update global max to handle case where path may go through the node
        self.global_max = max(self.global_max, left_max + node.val + right_max)
        return node.val + max(left_max, right_max)

    def solution_maintaining_3_states(self, root: Optional[TreeNode]):
        self.min_ = float('-inf')

        def find_min(node: TreeNode) -> int:
            if node is not None:
                self.min_ = max(node.val, self.min_)
                find_min(node.left)
                find_min(node.right)

        find_min(root)
        if self.min_ < 0:
            return self.min_

        @functools.lru_cache(None)
        def max_sum(node: TreeNode, is_part: bool, is_curved: bool) -> int:

            if node is None:
                return 0
            # print(node.val, is_part, is_curved)
            # case 1 - path includes node
            if is_part:
                if is_curved:
                    ans = node.val + max(max_sum(node.left, True, False) + max_sum(node.right, True, False), 0)
                    # print(ans)
                    return ans
                else:
                    # is not curved
                    ans = node.val + max(max_sum(node.left, True, False), max_sum(node.right, True, False), 0)
                    # print(ans)
                    return ans
            else:
                # could either be curved left or right or stratight or anything else
                left_max_sum = max(max_sum(node.left, True, True), max_sum(node.left, True, False),
                                   max_sum(node.left, False, False))
                right_max_sum = max(max_sum(node.right, True, True), max_sum(node.right, True, False),
                                    max_sum(node.right, False, False))
                ans = max(left_max_sum, right_max_sum, 0)
                # print(left_max_sum, right_max_sum, ans)
                return ans

        return max(max_sum(root, True, True), max_sum(root, True, False), max_sum(root, False, False))