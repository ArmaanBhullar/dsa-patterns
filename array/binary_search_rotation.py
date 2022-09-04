from typing import List
"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def find_num_rotation(ls: List):
            """
            returns number of rotation
            """
            start = 0
            end = len(ls) - 1
            mid = (start + end) // 2
            if ls[start] < ls[end]:
                return 0
            while end - start > 1:
                if ls[mid] >= ls[start]:
                    start = mid
                else:
                    end = mid
                mid = (start + end) // 2
            if ls[start] < ls[end]:
                return start
            else:
                return end

        k = find_num_rotation(nums)
        # print(k)
        start = k
        end = n - 1 + k
        mid = (start + end) // 2
        while end - start > 1:
            if nums[mid % n] >= target:
                end = mid
            else:
                start = mid
            mid = (start + end) // 2
        if nums[start % n] == target:
            return start % n
        elif nums[end % n] == target:
            return end % n
        else:
            return -1