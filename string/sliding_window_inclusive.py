"""
https://leetcode.com/problems/minimum-window-substring/description/
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        word_count = defaultdict(int)
        for letter in t:
            word_count[letter] += 1
        freq = defaultdict(int)
        i, j = 0, 0
        n = len(s)
        soln = ""

        def part_of(d1: Dict, d2: Dict) -> bool:
            for key in d1.keys():
                if d1[key] > d2[key]:
                    return False
            return True

        no_soln = True
        freq[s[j]] += 1
        while (j < n) and (i < n):
            if part_of(word_count, freq):
                candidate = s[i: j + 1]
                # print(candidate)
                if no_soln:
                    soln = candidate
                    no_soln = False
                if len(candidate) < len(soln):
                    soln = candidate
            # print(i, j, freq)
            if freq[s[i]] > word_count[s[i]]:
                # print("left")
                freq[s[i]] -= 1
                i += 1
            else:
                # print("right")
                j += 1
                if j < n:
                    freq[s[j]] += 1

        return soln

