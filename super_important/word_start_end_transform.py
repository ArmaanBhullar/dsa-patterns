"""
https://leetcode.com/problems/word-ladder/submissions/
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        # how to define the graph? -
        k = len(beginWord)
        wordList.append(beginWord)
        ls = deque([(1, beginWord)])
        seen = {word: False for word in wordList}
        graph = {word:[] for word in wordList}
        word_dict = defaultdict(set)
        for idx in range(len(wordList)):
            word = wordList[idx]
            shingles = []
            for i in range(k):
                shingle = word[:i] + '*' + word[i+1:]
                word_dict[shingle].add(word)
        # print(word_dict)
        seen[beginWord] = True
        while len(ls) > 0:
            cur_dist, cur_word = ls.popleft()
            if cur_word == endWord:
                return cur_dist
            neighbor_ls = []
            for i in range(k):
                shingle = cur_word[:i] + '*' + cur_word[i+1:]
                # print(shingle)
                for word in word_dict[shingle]:
                    if not seen[word] and word != cur_word:
                        neighbor_ls.append(word)
            neighbor_ls = list(set(neighbor_ls))
            # print("\n", cur_word, neighbor_ls, seen,)
            for neighbor in neighbor_ls:
                seen[neighbor] = True
                ls.append((cur_dist+1, neighbor))
        return 0