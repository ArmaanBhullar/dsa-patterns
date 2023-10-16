# TODO check solution for https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        t = len(word)
        ls = [] # ls[i] has the answers
        def get_pot_list(node):
            ans = []
            x = node[0]
            y = node[1]
            if x > 0:
                ans.append((x-1, y))
            if x < m-1:
                ans.append((x+1, y))
            if y > 0:
                ans.append((x, y-1))
            if y < n-1:
                ans.append((x, y+1))
            return ans

        def find_paths(k):
            # return all paths which form word[:k+1]
            prev_paths = ls[k-1-1]
            # print(k, prev_paths)
            all_paths = []
            for path in prev_paths:
                end_node = path[-1]
                pot_list = get_pot_list(end_node)
                for pot in pot_list:
                    if pot not in path:
                        if board[pot[0]][pot[1]] == word[k-1]:
                            path_copy = path.copy()
                            path_copy.append(pot)
                            all_paths.append(path_copy)
            return all_paths
        # initialize ls
        from collections import defaultdict
        word_dict = defaultdict(list)
        ls_start = []
        for i in range(m):
            for j in range(n):
                word_dict[board[i][j]].append((i, j))
                if board[i][j] == word[0]:
                    ls_start.append([(i, j)])
        ls.append(ls_start)
        if len(ls[0]) == 0:
            return False
        for c in word:
            if c not in word_dict:
                return False
        for i in range(2, len(word)+1):
            next_paths = find_paths(i)
            ls.append(next_paths)
            if len(next_paths) == 0:
                return False
        # print(ls)
        return True
