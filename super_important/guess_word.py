"""
https://leetcode.com/problems/guess-the-word/description/
"""
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        # sort words by place, char occurance
        place_dict = defaultdict(int)
        for word in words:
            for idx, char in enumerate(word):
                place_dict[str(idx) + char] += 1

        def sameness(word: str) -> int:
            score = 0
            for idx, char in enumerate(word):
                score += place_dict[str(idx) + char]
            return -1 * score

        words.sort(key=sameness)
        print(words)
        from functools import lru_cache
        @functools.lru_cache(None)
        def find_sim(x: int, y: int) -> int:
            sim = 0
            for i in range(6):
                sim += int(words[x][i] == words[y][i])
            return sim

        n = len(words)
        self.rule_out = {}

        def rule_out_words(x: int, sim: int) -> None:
            # adds words with sim >= sim to the rule out dict
            for i in range(n):
                if i != x:
                    if find_sim(i, x) != sim:
                        self.rule_out[i] = find_sim(i, x)

        for i in range(n):
            if i not in self.rule_out:
                master_sim = master.guess(words[i])
                rule_out_words(i, master_sim)
