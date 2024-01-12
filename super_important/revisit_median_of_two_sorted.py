"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2

        def solve(k, start_1, end_1, start_2, end_2):
            # print(k, start_1, end_1, start_2, end_2)
            # if segment of one array is empty => we've discarded all the stuff from that segment and we simply return the corresponding element fromt he remaining array
            if start_1 > end_1:
                return nums2[k - start_1]
            if start_2 > end_2:
                return nums1[k - start_2]

            # get the middle index and middle values of the two arrays
            idx_1, idx_2 = (start_1 + end_1) // 2, (start_2 + end_2) // 2
            val1, val2 = nums1[idx_1], nums2[idx_2]

            # if k is in the right half of nums1. + nums2, remove smaller left half of nums1
            if k > idx_1 + idx_2:
                if val1 > val2:
                    return solve(k, start_1, end_1, idx_2 + 1, end_2)
                else:
                    return solve(k, idx_1 + 1, end_1, start_2, end_2)
            # Otherwise, remove the larger half
            else:
                if val1 > val2:
                    return solve(k, start_1, idx_1 - 1, start_2, end_2)
                else:
                    return solve(k, start_1, end_1, start_2, idx_2 - 1)

        if n % 2 == 1:
            return solve(n // 2, 0, n1 - 1, 0, n2 - 1)
        else:
            return (solve(n // 2 - 1, 0, n1 - 1, 0, n2 - 1) + solve(n // 2, 0, n1 - 1, 0, n2 - 1)) / 2
