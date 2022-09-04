from typing import List
# https://leetcode.com/problems/is-graph-bipartite/submissions/
"""
Main idea is if the graph is unconnected, then iterate over all the nodes and in each iteration, do a dfs. Maintain a 
visited set to keep track of if a node is visited. When inserting the node in queue or stack depending on bfs or dfs, 
insert it in the unvisited set also
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = set()
        import queue
        color = [0 for i in range(n)]

        for node in range(n):
            # print(node, visited)
            if node not in visited:
                q = queue.Queue()
                q.put(node)
                color[node] = 1
                visited.add(node)
                while not q.empty():
                    cur = q.get() # color has already been assigned
                    for neighbor in graph[cur]:
                        # print(cur, neighbor)
                        if color[neighbor] == 0:
                            color[neighbor] = -1*color[cur]
                            q.put(neighbor)
                            visited.add(neighbor)
                        elif color[neighbor] == color[cur]:
                            return False
                        else:
                            pass
        return True