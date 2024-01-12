"""
https://leetcode.com/problems/maximum-length-of-pair-chain/description/
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sort by end times
        pairs = sorted(pairs, key=lambda x: x[1])
        idx = 0
        n = len(pairs)
        counter = 0
        while idx < n:
            counter += 1
            # pick first end and then the next end and so on, greedily
            end = pairs[idx][1]
            while (idx < n) and (pairs[idx][0] <= end):
                idx += 1  # skip all which overlap with this
        return counter

