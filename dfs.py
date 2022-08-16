from typing import List, Dict
from collections import defaultdict

class DFS:

    def dfs(self, adj_list: Dict[int, List[int]], start: int, end: int):
        # maintain a stack for dfs
        ls = list()
        ls.append(start)
        visited = set()
        visited.add(start)
        found = False
        while (len(ls) > 0) and (not found):
            cur_node = ls.pop()
            for neighbor in adj_list[cur_node]:
                print(neighbor)
                if neighbor == end:
                    found = True
                if neighbor not in visited:
                    visited.add(neighbor)
                    ls.append(neighbor)
        return found


if __name__ == "__main__":
    d = defaultdict(list)
    d[0] = [1, 2, 3]
    d[1] = [3, 4, 5]
    d[9] = [5, 1, 10]
    d[5] = [9]
    d[10] = [4]
    d[11] = [10]
    d[12] = [7]
    dfs = DFS()
    print(dfs.dfs(adj_list=d, start=0, end=9))
    print(dfs.dfs(adj_list=d, start=4, end=12))
