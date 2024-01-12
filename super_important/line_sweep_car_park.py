"""
https://leetcode.com/problems/points-that-intersect-with-cars/description/
"""

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        max_lim = max([x[1] for x in nums])
        x_line = [0 for idx in range(max_lim + 1)]
        for start, end in nums:
            x_line[start - 1] += 1
            x_line[end] += -1
        cnt = 0
        cum_sum = 0
        for idx in range(max_lim + 1):
            cum_sum += x_line[idx]
            if cum_sum != 0:
                cnt += 1
        # print(x_line)
        return cnt


