"""
https://leetcode.com/problems/sliding-window-maximum/editorial/
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a heap of all elements seen so far
        # maintain a counter which maintains the count of elements in the heap
        # use oth of these to proceed
        # start
        import heapq
        n = len(nums)
        ls = [-1 * nums[idx] for idx in range(k)]
        heapq.heapify(ls)
        cnt = defaultdict(int)
        for idx in range(k):
            cnt[nums[idx]] += 1  # setup counts in heaps
        ans = [None for idx in range(n - k + 1)]
        if len(ans) >= 1:
            ans[0] = -1 * ls[0]
        for idx in range(0, len(ans) - 1):
            # progress by 1
            heapq.heappush(ls, -1 * nums[idx + k])
            cnt[nums[idx]] -= 1
            cnt[nums[idx + k]] += 1
            # find current max
            # print(idx, ans, ls)
            max_el = -1 * heapq.heappop(ls)
            # cleanup of heap by lazy delete
            while cnt[max_el] == 0:
                max_el = -1 * heapq.heappop(ls)
            ans[idx + 1] = max_el
            # push the max back in
            heapq.heappush(ls, -1 * max_el)
            # remove element from heap
        return ans

class FasterSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a dq s.t. the elements of dq are indices (monotonically increasing)
        # and the values of nums[idx] are also monotonic increasing
        # we maintain this by popping any elemtns smaller than the new addition since they will never be selected as answer given the new element is bigger than them and on the right
        from collections import deque
        dq = deque([])
        ans = []
        # step 1 build the initial dq and the first answer
        for idx in range(k):
            while len(dq) > 0 and nums[idx] > nums[dq[-1]]:
                dq.pop() # remove
            dq.append(idx)
        ans.append(nums[dq[0]])
        for idx in range(k, len(nums)):
            # print(dq)
            # first increment by 1 then populate answer
            if len(dq) > 0 and dq[0] == idx - k:
                dq.popleft() # invariant is still maintained
            # now we add the new element
            while len(dq)>0 and  nums[idx] > nums[dq[-1]]:
                dq.pop()
            dq.append(idx)
            ans.append(nums[dq[0]])
        return ans



