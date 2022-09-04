class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # this is a toplogical sort
        # start by computing in degree and out degree of all nodes
        indegree = [0 for i in range(numCourses)]
        outdegree = [0 for i in range(numCourses)]
        # convert to graph representatoin
        from collections import defaultdict
        import queue
        graph = defaultdict(list)
        for dst, src in prerequisites:
            graph[src].append(dst)
            indegree[dst] += 1
            outdegree[src] += 1
        ls_order = []
        visited = set()
        is_dag = True
        # initialize queue
        q = queue.Queue()
        for i in range(numCourses):
            if (indegree[i] == 0) and (i not in visited):
                q.put(i)
        while (len(visited) < numCourses) and is_dag:  # while there are unvisited nodes
            # add all indegree = 0 nodes to q

            # Now expand into q
            # print(q.queue)
            if q.empty():
                is_dag = False  # nowhere to start with!
            else:
                while (not q.empty()):
                    cur_node = q.get()
                    ls_order.append(cur_node)
                    for neighbor in graph[cur_node]:
                        indegree[neighbor] -= 1  # reduce indegree
                        if indegree[neighbor] == 0: # check if this is now a candidate for being put in queue
                            q.put(neighbor)
                    visited.add(cur_node)
        if is_dag:
            return ls_order
        else:
            return []


