"""
https://leetcode.com/problems/meeting-rooms-ii/submissions/
"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # O n*logn solution
        # simulate the problem by1
        # Sorting ascending by start time
        # creating a heap initialize with end time
        # For each in sorted start times - check if top of heap has less than this as start time, if so, pop it
        # Add a new room on the top of heap
        import heapq
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 0:
            return 0
        heap = []
        heapq.heappush(heap, intervals[0][1])
        n = len(intervals)
        for i in range(1, n):
            start, end = intervals[i]

            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            # print(end, heap)
        return len(heap)
        # This is O n*n
        # intervals.sort(key = lambda x: x[0])
        # n = len(intervals)
        # max_so_far = 1
        # # print(intervals)
        # for i in range(1, n):
        #     start, end = intervals[i]
        #     count_overlaps = 1
        #     for j in range(i):
        #         if intervals[j][1] > start:
        #             count_overlaps += 1
        #         # print(i, j, count_overlaps)
        #     max_so_far = max(max_so_far, count_overlaps)
        # return max_so_far