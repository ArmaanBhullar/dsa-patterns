from typing import List
"""
https://leetcode.com/problems/possible-bipartition/
"""

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # DFS while marking people in groups, if an already grouped person conflicts, return Falsem else True

        groups = [0 for i in range(n + 1)]  # +1 and -1 final values, 0 => unassigned

        from collections import defaultdict
        graph = defaultdict(list)
        for p1, p2 in dislikes:
            graph[p1].append(p2)
            graph[p2].append(p1)

        for node in range(1, n + 1):
            if groups[node] == 0:
                # assign and do dfs from here
                groups[node] = 1
                ls = [node]
                while len(ls) > 0:
                    cur = ls.pop()
                    for neighbor in graph[cur]:

                        if groups[neighbor] == groups[cur]:
                            return False  # end, not possible
                        elif groups[neighbor] == 0:
                            # assign
                            groups[neighbor] = -1 * groups[cur]
                            ls.append(neighbor)
                        else:
                            pass  # already assigned through some other path
        return True
