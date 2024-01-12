"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # find overlapping intervals basically and count how many times the heap goes to zero
        points = sorted(points, key = lambda x: x[1]) # sort by x_start coordinate
        counter = 0
        idx = 0
        while idx < len(points):
            # find end of the current baloon and advance idx to next
            counter += 1
            end = points[idx][1]
            while idx < len(points) and points[idx][0] <= end:
                idx += 1 # pass over this point
        return counter