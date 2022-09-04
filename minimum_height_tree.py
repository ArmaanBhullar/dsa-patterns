class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        from collections import defaultdict
        graph = defaultdict(list)
        degree = [0 for i in range(n)]
        generation = [0 for i in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
            degree[src] += 1
            degree[dst] += 1

        import queue
        q = queue.Queue()

        for i in range(n):
            if degree[i] == 1:
                q.put(i)
        visited = set()
        while len(visited) < n:
            # print(q.queue)
            cur = q.get()
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        generation[neighbor] = generation[cur] + 1
                        q.put(neighbor)
            # Mark as visited only after you're done processing the node completely!
            visited.add(cur)
        
        max_generation = max(generation)
        ls_new = []
        for i in range(n):
            if generation[i] == max_generation:
                ls_new.append(i)
        return ls_new
