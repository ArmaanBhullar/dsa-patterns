"""
https://leetcode.com/problems/non-overlapping-intervals/
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        num_excluded = 0
        prev_end = intervals[0][1]
        # print(intervals)
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # print(prev_end, start, end, num_excluded)
            if start >= prev_end:  # case 1 exclusive, include this
                prev_end = end
            elif end < prev_end:  # case 2 fully included
                prev_end = end
                num_excluded += 1
            else:
                # partial overlap, exclude new one
                num_excluded += 1
        return num_excluded

#         intervals.sort(key = lambda x: x[0])
#         n = len(intervals)
#         dp = [1 for i in range(n)]


#         for i in range(1, n):
#             # max_if_included
#             j = i-1
#             found = False
#             while (j>=0 and not found):
#                 if not (intervals[j][1] > intervals[i][0]):
#                     dp[i] = 1 + dp[j]
#                     found = True
#                 j -= 1
#             # max if not included
#             if dp[i-1] > dp[i]:
#                 dp[i] = dp[i-1]
#         return n - dp[-1]
