from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # essentially we have to find the MST. step 1 is to fetch all edges and sort by weight ascending (the default
        # .sort(key=) method) step 2 is to start adding edges smaller to larger, using union find while checking that
        # 2 nodes are not already connected
        n = len(points)
        edges = []
        for i in range(n):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, n):
                x2 = points[j][0]
                y2 = points[j][1]
                edges.append((i, j, abs(x1 - x2) + abs(y1 - y2)))

        # quick find and rank union
        root = list(range(n))
        rank = [1 for i in range(n)]

        def find(x: int) -> int:
            # with path compression
            # return root of node x
            if x == root[x]:
                return x
            ls = []
            while (x != root[x]):
                ls.append(x)
                x = root[x]
            for node in ls:
                root[node] = x
            rank[x] = 1
            return x

        def union(x: int, y: int):
            root_x = find(x)
            root_y = find(y)
            if rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                root[root_x] = root_y
            else:
                root[root_x] = root_y
                rank[root_y] += 1

        def connected(x: int, y: int) -> bool:
            return find(x) == find(y)

        # kruskals
        edges.sort(key=lambda x: x[2])  # default is ascending
        path_sum = 0
        num_edges = 0
        # print(edges)
        for (i, j, weight) in edges:
            if not connected(i, j):
                union(i, j)
                # print(i, j, weight)
                path_sum += weight
                num_edges += 1
            if num_edges == n - 1:
                break

        return path_sum


