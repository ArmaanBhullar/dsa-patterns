"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach n*logn - Patience sort
        # As you go over the array, create heaps (lists) with following strategy -
        # Never place a larger card on a smaller list
        # For each card, place it in the leftmost eligible list
        # Number of lists gives you the longest increasing subsequence length, the exact sequence is a bit tricky
        def binary_search(ls: List[int], target: int) -> int:
            """
            Returns the index of first list where element is larger than target
            """
            start = 0
            end = len(ls) - 1
            mid = (start + end) // 2
            while end - start > 1:
                if ls[mid] >= target:  # search in left part
                    end = mid
                else:  # search in right part
                    start = mid
                mid = (start + end) // 2
            # Upto here this binary search is generic, what you do from here on is what gives the flavor, e.g. here we want first element larger than or equalt to the target
            # for some other question, we may want to focus on equality
            if ls[start] >= target:
                return start
            if ls[end] >= target:
                return end
            return -1  # no larger element found

        n = len(nums)
        heaps = [[nums[0]]]  # List of Heaps which are lists themselves
        max_element_for_each_heap = [nums[0]]
        for i in range(1, n):
            # find which heap this card element to?
            k = binary_search(max_element_for_each_heap, nums[i])
            # Place element on this heap
            if k != -1:
                heaps[k].append(nums[i])
                max_element_for_each_heap[k] = nums[i]  # update max element
            else:
                # create a new heap with this element
                heaps.append([nums[i]])
                max_element_for_each_heap.append(nums[i])  # update max element
        # print(heaps)
        return len(
            heaps)  # this is the longest subsequence length, for the subsequence itself it's a bit more fight in constant time
        # print(sequence)

        ## O n*n solution
#         n = len(nums)

#         lis = [1 for i in range(n)]
#         for i in range(1, n):
#             # find highest lis for 0 .. i-1 which are less than nums[i]
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     lis[i] = max(lis[i], 1 + lis[j])
#         return max(lis)