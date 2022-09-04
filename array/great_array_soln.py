"""
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # first sort and store sorted indices, compute maximum and minimum indices and then do simple comparision
        n = len(height)
        sorted_height_indices_tuple = sorted(list(enumerate(height)), key = lambda x: x[1])
        sorted_indices = [x[0] for x in sorted_height_indices_tuple]
        sorted_height = [x[1] for x in sorted_height_indices_tuple]
        max_index_to_right = [0 for i in range(n)]
        min_index_to_right = [0 for i in range(n)]
        max_so_far = sorted_indices[-1]
        min_so_far = sorted_indices[-1]
        for i in range(n):
            max_index_to_right[n-1-i] = max_so_far
            max_so_far = max(max_so_far, sorted_indices[n-1-i])
            min_index_to_right[n-1-i] = min_so_far
            min_so_far = min(min_so_far, sorted_indices[n-1-i])
        max_vol_so_far = 0
        for wall_index in range(n):
            right_container_volume = sorted_height[wall_index]*(max_index_to_right[wall_index] - sorted_indices[wall_index])
            left_container_volume = sorted_height[wall_index]*(sorted_indices[wall_index] - min_index_to_right[wall_index])
            max_vol_so_far = max(max_vol_so_far, right_container_volume, left_container_volume)
        return max_vol_so_far
        ## Alternate and much faster solution
        # n = len(height)
        # start = 0
        # end = n - 1
        # max_area = 0
        # while start < end:
        #     max_area = max(max_area, (end - start) * min(height[start], height[end]))
        #     if height[start] < height[end]:
        #         start += 1
        #     else:
        #         end -= 1
        # return max_area
