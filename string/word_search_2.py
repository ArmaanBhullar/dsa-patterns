"""
Didn't solve TLE but is otherwise great soln, 63/64 pass. TODO check if we can do recursion more easily than iterative DFS

"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # implement a trie based on words and recursively check for ewach cell on board what all it matches with and add if we reach end somewhere
        m = len(board)
        n = len(board[0])
        word_set = set()
        self.word_cnt = 0
        for i in range(m):
            for j in range(n):
                word_set.add(board[i][j])
        trie = {}  # implemented as a dictionary
        self.ls = set()

        def insert(node: dict, word: str) -> None:
            for char in word:
                node = node.setdefault(char, {})
                node["ref"] = node.get("ref", 0) + 1  # increment ref counter
            node["$"] = word  # mark as end of a word here

        for word in words:
            if set(word).difference(word_set) == set():
                insert(trie, word)
                self.word_cnt += 1

        # print(trie)

        def dfs(x: int, y: int, trie: dict) -> None:
            ls = [((x, y), set([(x, y)]), trie)]
            while len(ls) > 0:
                # print(ls)
                # go over each neighbor in path and check
                (cur_x, cur_y), visited, tr = ls.pop()
                if "$" in tr:
                    # mark word as being present
                    self.ls.add(tr["$"])
                    tr.pop("$")
                    self.word_cnt -= 1
                    tr["ref"] -= 1
                # iterate over neighbors
                for x_off, y_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x_n, y_n = cur_x + x_off, cur_y + y_off
                    # print(x_n, y_n)
                    if x_n >= 0 and y_n >= 0 and x_n < m and y_n < n:
                        # print(board[x_n][y_n], tr)
                        # valid neighbor, check if it matches with trie?
                        if (board[x_n][y_n] in tr) and ((x_n, y_n) not in visited) and (tr["ref"] > 0):
                            new_visited = visited.copy()
                            new_visited.add((x_n, y_n))
                            ls.append(
                                ((x_n, y_n), new_visited, tr[board[x_n][y_n]])
                            )

        # now we have a trie, let's go search for each cell

        for i in range(m):
            for j in range(n):
                if self.word_cnt > 0:
                    if board[i][j] in trie:
                        dfs(i, j, trie[board[i][j]])
        return list(self.ls)