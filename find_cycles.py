class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # implement BFS and detect cycle
        from collections import defaultdict
        graph = defaultdict(list)
        import queue
        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        # completes graph construction

        temp_start = 0
        overall_visited = set()
        unvisited = set(range(numCourses))
        while (len(unvisited) > 0):
            stack = []
            visited = set()
            stack.append((temp_start, []))
            while len(stack) != 0:
                # print(q.queue)
                cur_node, cur_path = stack.pop()
                for neighbor in graph[cur_node]:
                    if neighbor in cur_path:
                        return False
                    new_path = cur_path.copy()
                    new_path.append(cur_node)
                    stack.append((neighbor, new_path))
                visited.add(cur_node)
            # at this point, select next subset
            # print(visited)
            overall_visited = overall_visited.union(visited)
            # print(overall_visited)
            unvisited = set(range(numCourses)).difference(set(overall_visited))
            # print(unvisited)
            if len(unvisited) > 0:
                temp_start = list(unvisited)[0]

        return True