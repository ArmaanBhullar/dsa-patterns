"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)
        lo = 0
        hi = 2 * n2
        while lo <= hi:

            mid2 = (hi + lo) // 2
            mid1 = n1 + n2 - mid2
            print(lo, hi, mid1, mid2)
            if mid1 == 0:
                L1 = float('-inf')
            else:
                L1 = nums1[(mid1 - 1) // 2]
            if mid1 == 2 * n1:
                R1 = float('inf')
            else:
                R1 = nums1[mid1 // 2]
            if mid2 == 0:
                L2 = float('-inf')
            else:
                L2 = nums2[(mid2 - 1) // 2]
            if mid2 == 2 * n2:
                R2 = float('inf')
            else:
                R2 = nums2[mid2 // 2]

            # update step
            if L1 > R2:
                lo = mid2 + 1
            elif L2 > R1:
                hi = mid2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2