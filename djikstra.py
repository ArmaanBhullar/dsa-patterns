from collections import defaultdict
from typing import List
import heapq


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for src, dst, time in times:
            graph[src].append((dst, time))  # construct graph with node, weight

        visited = set()

        table = defaultdict(tuple)  # table[1] = (time_so_far, previous_node) = (5, 2)

        for i in range(1, n + 1):
            table[i] = (float('inf'), k)  # everything is at infinite dist from k in the beginning # initialize table

        table[k] = (0, k)  # k is at 0 distance from k
        visit_list = [(0, k)]  # start from k

        while (len(visited) < n) and len(visit_list) != 0:  # while there are nodes to be visited AND the heap is
            # get the top of heap = node with least distance from source so
            current_dist, current_node = heapq.heappop(visit_list)
            edges = graph[current_node]
            for edge in edges:
                destination = edge[0]
                distance = edge[1]
                if destination not in visited:  # if we've already visited this node then it's analysis is complete,
                    # skip this
                    current_min_distance = table[destination][0]
                    candidate_min_distance = table[current_node][0] + distance
                    if current_min_distance > candidate_min_distance:
                        # update table entry
                        table[destination] = (candidate_min_distance, current_node)
                        heapq.heappush(visit_list, (table[destination][0], destination))  # Only if we update distance
                        # to node do we add a new entry to the heap

            visited.add(current_node)  # after going over all the edges, mark this node as visited

        if len(visited) < n:  # parts of the graph are not reachable
            return -1
        # finish when all are unvisited
        # return maximum entry in the table
        minim = float('-inf')
        for i in range(1, n + 1):
            if table[i][0] > minim:
                minim = table[i][0]
        return minim
