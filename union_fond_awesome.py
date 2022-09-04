from typing import List
"""
https://leetcode.com/problems/regions-cut-by-slashes/
"""

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # break each square into 4 spaces. Then connect these accorsing to rules defined by tghe geometric shapes in these
        # finally, do a union find and count disconnected components
        num_squares = len(grid) * len(grid)
        n = 4 * num_squares
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(x: int) -> int:

            if x == root[x]:
                return x
            else:
                ls = []
                while x != root[x]:
                    ls.append(x)
                    x = root[x]
                for node in ls:
                    root[node] = x
                rank[x] = 1
            return x

        def union(x: int, y: int) -> None:
            # print(x, y)
            root_x = find(x)
            root_y = find(y)
            if root_x != root[y]:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_x] = root_y
                    rank[root_y] += 1

        full_grid = "".join(grid)

        for square_number in range(num_squares):

            if full_grid[square_number] == '/':
                union(4 * square_number, 4 * square_number + 3)
                union(4 * square_number + 1, 4 * square_number + 2)
                # connect 0 and 3
                # connect 1 and 2
            if full_grid[square_number] == '\\':
                union(4 * square_number, 4 * square_number + 1)
                union(4 * square_number + 3, 4 * square_number + 2)
                # connect 0 and 1
                # connect 3 and 2
            if full_grid[square_number] == ' ':
                union(4 * square_number, 4 * square_number + 1)
                union(4 * square_number, 4 * square_number + 2)
                union(4 * square_number, 4 * square_number + 3)
                # connect 0 and 1
                # connect 0 and 2
                # connect 0 and 3
        for i in range(len(grid)):
            for j in range(len(grid)):
                # for cell i, j
                cell_number = len(grid) * i + j
                # print(i, j, cell_number)
                # connect left
                if j > 0:
                    union(4 * cell_number + 3, 4 * (cell_number - 1) + 1)
                    # print("1", 4*cell_number+3)
                # connect front
                if j < len(grid) - 1:
                    union(4 * cell_number + 1, 4 * (cell_number + 1) + 3)
                    # print("2")
                # connect top
                if i > 0:
                    top_cell_number = len(grid) * (i - 1) + j
                    union(4 * cell_number + 0, 4 * top_cell_number + 2)
                    # print("3", 4*cell_number + 0, 4*top_cell_number + 2)
                # connect bottom
                if i < len(grid) - 1:
                    bottom_cell_number = len(grid) * (i + 1) + j
                    # print("4", 4*cell_number + 2, 4*bottom_cell_number + 0)
                    union(4 * cell_number + 2, 4 * bottom_cell_number + 0)

        return len(set([find(i) for i in range(n)]))