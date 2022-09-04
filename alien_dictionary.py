from collections import OrderedDict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        edges = []
        all_chars = set()
        global wrong_ordering
        wrong_ordering = False

        # main task is to get the edges between characters
        def extract_edges(words):
            global wrong_ordering
            if len(words) != 0:
                tmp_ls = []
                prev_char = words[0][0]
                all_chars.add(prev_char)
                tmp_ls.append(prev_char)
                for i in range(len(words)):
                    first_char = words[i][0]
                    all_chars.add(first_char)
                    if first_char != prev_char:
                        tmp_ls.append(first_char)
                        prev_char = first_char
                # [w, e, r]
                # add the edges
                for i in range(len(tmp_ls)):
                    if i > 0:
                        edges.append((tmp_ls[i - 1], tmp_ls[i]))
                # edges = [[e, w], (r, e)]
                # now the recursive step

                for first_char in tmp_ls:
                    new_list = []
                    not_empty_encountered = False
                    for j in range(len(words)):
                        if words[j][0] == first_char:
                            new_word = words[j][1:]
                            # print(f"{first_char}, {new_word}, {wrong_ordering}, {not_empty_encountered}")
                            if len(new_word) > 0:
                                not_empty_encountered = True
                                new_list.append(new_word)
                            else:
                                if not_empty_encountered == True:  # then this is bad
                                    wrong_ordering = True

                    extract_edges(new_list)

        # wrong_ordering = False
        extract_edges(words)
        if wrong_ordering:
            return ""
        # print(edges)
        n = len(all_chars)
        # print(all_chars)
        # now form a graph from above edges
        from collections import defaultdict
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for src, dst in edges:
            graph[src].append(dst)
            indegree[dst] += 1

        print(graph)
        # initialize queue
        import queue
        q = queue.Queue()
        for char in list(all_chars):
            if indegree[char] == 0:
                q.put(char)
        visited = set()
        is_dag = True
        global_order = []
        while (len(visited) < n) and is_dag:
            if q.empty():
                is_dag = False
            else:
                cur_char = q.get()
                if cur_char in visited:
                    is_dag = False
                else:
                    global_order.append(cur_char)
                    for neighbor in graph[cur_char]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            q.put(neighbor)
                    visited.add(cur_char)
        if not is_dag:
            return ""
        else:
            return "".join(global_order)










