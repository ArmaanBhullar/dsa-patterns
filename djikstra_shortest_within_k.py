from typing import List
"""
Djikstra within k steps
https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/

"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # we'll use Djikstra to calculate least weighted path but also consider paths which are shorter
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)

        for src1, dst1, price in flights:
            graph[src1].append((dst1, price))

        # table of distances
        table = {}  # current cost, last destination, number of hops so far inclusive of current
        for i in range(n):
            table[i] = (float('inf'), None, 0)

        heap = [(0, src, 0)]  # cost, node, number of hops inclusive
        visited = [False for i in range(n)]

        while (False in visited) and len(heap) > 0:
            cur_cost, cur_node, cur_hops = heapq.heappop(heap)

            for neighbor, cost in graph[cur_node]:
                cost_from_cur_node = cost + cur_cost
                hops_from_src_cur_node = cur_hops + 1
                if visited[neighbor] == False:
                    if (hops_from_src_cur_node <= k + 1) and (cost_from_cur_node < table[neighbor][0]):
                        # update table and add to heap
                        table[neighbor] = (cost_from_cur_node, cur_node, hops_from_src_cur_node)
                        heapq.heappush(heap, (cost_from_cur_node, neighbor, hops_from_src_cur_node))

                if hops_from_src_cur_node < table[neighbor][
                    2]:  # if you found a shorter, more costly path, add this to heap too
                    heapq.heappush(heap, (cost_from_cur_node, neighbor, hops_from_src_cur_node))

            visited[cur_node] = True

        dst_cost = table[dst][0]
        if dst_cost == float('inf'):
            return -1
        else:
            return dst_cost

