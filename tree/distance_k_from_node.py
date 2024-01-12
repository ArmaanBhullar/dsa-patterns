"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/editorial/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # do in 2 parts 1) define a fn which returns in child tree at distance k
        # 2) find path to node from root
        # 3) run fn on targetwith k
        # 4) run fn on each parent of target with k-distance to parent
        if k == 0:
            return [target.val]
        path_to_node, direction = self.bfs(root, target.val)
        # print([node.val for node in path_to_node])
        ans_ls = []
        ans_ls.extend(self.distance_k_children(target, k))
        # print(ans_ls)
        for idx, (node, direct) in enumerate(zip(path_to_node[::-1][:k], direction[::-1][:k])):
            # print(idx, node.val)
            if k - idx - 1 == 0:
                ans_ls.append(node.val)
            else:
                if direct == 'l':
                    ans_ls.extend(self.distance_k_children(node.right, k - idx - 2))
                else:
                    ans_ls.extend(self.distance_k_children(node.left, k - idx - 2))

        return ans_ls

    def bfs(self, root_node: TreeNode, val: int):
        ls = deque([([], root_node, [])])
        while (len(ls) > 0):
            cur_path, cur_node, direction = ls.popleft()  # use deque
            if cur_node.val == val:
                return cur_path, direction
            if cur_node.left is not None:
                # add to ls
                left_path_copy = list(cur_path)
                left_direction_copy = list(direction)
                left_direction_copy.append('l')
                left_path_copy.append(cur_node)
                ls.append((left_path_copy, cur_node.left, left_direction_copy))
            if cur_node.right is not None:
                # add to ls
                right_path_copy = list(cur_path)
                right_direction_copy = list(direction)
                right_direction_copy.append('r')
                right_path_copy.append(cur_node)
                ls.append((right_path_copy, cur_node.right, right_direction_copy))

    def distance_k_children(self, root: TreeNode, k: int):
        # do BFS
        if not root:
            return []
        ls = deque([(0, root)])
        ans = []
        while len(ls) > 0:
            cur_dist, cur_node = ls.popleft()  # use deque
            if cur_dist == k:
                ans.append(cur_node.val)
            if cur_dist < k:
                if cur_node.left is not None:
                    ls.append((cur_dist + 1, cur_node.left))
                if cur_node.right is not None:
                    ls.append((cur_dist + 1, cur_node.right))
        return ans

