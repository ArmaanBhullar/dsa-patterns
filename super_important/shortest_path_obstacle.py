##### Approach 1
"""
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
"""

#### A* Solution
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        import queue
        m = len(grid)
        n = len(grid[0])
        if k >= m + n - 2:
            return m + n - 2

        def dist(x: int, y: int) -> int:
            return m - 1 - x + n - 1 - y

        # BFS with state space having (i, j, k)
        start = (dist(0, 0), 0, 0, 0, k)  # cost, steps, x, y, k
        visited = set([(0, 0, k)])  # don't keep steps in state
        q = []
        heapq.heappush(q, start)
        while q:
            # print(q)
            cost, steps, x, y, k_left = heapq.heappop(q)
            if (x == m - 1 and y == n - 1):
                return steps
            for x_delta, y_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x_new = x + x_delta
                y_new = y + y_delta
                k_new = k_left
                # print(x_new, y_new)
                if 0 <= x_new <= m - 1 and 0 <= y_new <= n - 1:
                    k_new -= grid[x_new][y_new]
                    if ((x_new, y_new, k_new) not in visited) and (k_new >= 0):
                        heapq.heappush(q, (steps + 1 + dist(x_new, y_new), steps + 1, x_new, y_new, k_new))
                        visited.add((x_new, y_new, k_new))

        return -1


class NormalSolution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        import queue
        m = len(grid)
        n = len(grid[0])
        if k >= m + n - 2:
            return m + n - 2

        # BFS with state space having (i, j, k)
        start = (0, 0, 0, k)  # x, y, steps, k
        visited = set([(0, 0, k)])  # don't keep steps in state
        q = deque([])
        q.append(start)
        while q:
            # print(q)
            x, y, steps, k_left = q.popleft()
            if (x == m - 1 and y == n - 1):
                return steps
            for x_delta, y_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x_new = x + x_delta
                y_new = y + y_delta
                k_new = k_left
                # print(x_new, y_new)
                if 0 <= x_new <= m - 1 and 0 <= y_new <= n - 1:
                    k_new -= grid[x_new][y_new]
                    if ((x_new, y_new, k_new) not in visited) and (k_new >= 0):
                        q.append((x_new, y_new, steps + 1, k_new))
                        visited.add((x_new, y_new, k_new))

        return -1









