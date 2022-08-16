from collections import defaultdict
from typing import List
import heapq

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for src, dst, time in times:
            graph[src].append((dst, time))

        visited = set()

        table = defaultdict(tuple)  # table[1] = (time_so_far, previous_node) = (5, 2)

        for i in range(1, n + 1):
            table[i] = (float('inf'), k)  # everything is at infinite dist from k in the beginning

        table[k] = (0, k)  # k is at 0 distance from k
        visit_list = [(0, k)]  # start from k

        while ((len(visited) < n) and len(visit_list) != 0):  # while there are nodes to be visited
            # go over all edges from unvisited node
            current_dist, current_node = heapq.heappop(visit_list)
            #             visit_list.sort(key = lambda x: -1*x[0])

            #             current_dist, current_node = visit_list.pop() # has shortest current path
            edges = graph[current_node]
            for edge in edges:
                destination = edge[0]
                distance = edge[1]
                if destination not in visited:
                    # check for all in table if shorter than one already in table?
                    current_min_distance = table[destination][0]
                    candidate_min_distance = table[current_node][0] + distance
                    if current_min_distance > candidate_min_distance:
                        # update table entry
                        table[destination] = (candidate_min_distance, current_node)
                        heapq.heappush(visit_list, (table[destination][0], destination))

            visited.add(current_node)

        if len(visited) < n:
            return -1  # parts of the graph are not reachable
        # finish when all are unvisited
        # return maximum entry in the table
        minim = float('-inf')
        for i in range(1, n + 1):
            if table[i][0] > minim:
                minim = table[i][0]
        return minim

