from typing import List, DefaultDict
from collections import defaultdict
d = defaultdict(list)
d["h"].append(76)
print(d["h"])
print(d["g"])

"""
BFS 
q = queue.Queue()
q.put(something)
# mark as visited here, not after fetch, somehow it's faster
q.get(something)
q.empty()

"""

class Solution:
    """
    BFS with iteration and queue
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        import queue
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]  # everything unvisited at the beginnig

        def bfs_island(i: int, j: int):
            # marks all places that can be visited from i, j on visited array
            bfs_q = queue.Queue()
            bfs_q.put((i, j))
            visited[i][j] = 1  # mark as visited
            while (not bfs_q.empty()):
                c_i, c_j = bfs_q.get()

                # find all edges connected to this and add to q if not visited
                for potential_neighbor in [(c_i + 1, c_j), (c_i, c_j + 1), (c_i - 1, c_j), (c_i, c_j - 1)]:
                    n_i = potential_neighbor[0]
                    n_j = potential_neighbor[1]
                    # only consider if within bounds
                    if (0 <= n_i < m) and (0 <= n_j < n):
                        # if is land and is not visited, add to q
                        if (grid[n_i][n_j] == "1") and (visited[n_i][n_j] == 0):
                            bfs_q.put((n_i, n_j))
                            visited[n_i][n_j] = 1

        island_counter = 0

        for i in range(m):
            for j in range(n):
                # print(f"calling with {i}, {j}, {island_counter}, {grid[i][j]=='1'}, {visited[i][j]==0}")
                if (visited[i][j] == 0) and grid[i][j] == "1":
                    # print(f"calling with {i}, {j}, {island_counter}")
                    bfs_island(i, j)
                    island_counter += 1

        return island_counter



