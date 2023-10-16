"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = {}
        n = len(s)
        i, j = 0, 0
        # initialize
        most_freq = s[0]
        ans = 0
        while j < n:
            # calc eplacement cost, if < k, then
            freq_dict[s[j]] = freq_dict.get(s[j], 0) + 1
            if freq_dict[s[j]] > freq_dict[most_freq]:
                most_freq = s[j]
            replacement_cost = j - i + 1 - freq_dict[most_freq]
            if replacement_cost <= k:
                # slide right
                # print(i, j, replacement_cost, k, freq_dict)
                ans = max(ans, j - i + 1)
            else:
                # slide left
                freq_dict[s[i]] -= 1
                i += 1
            j += 1
        return ans
