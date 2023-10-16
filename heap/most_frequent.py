"""
https://leetcode.com/problems/top-k-frequent-elements/description/
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put count and element in a heap, then construct set and keep popping till you get unique stuff
        counter = defaultdict(int)
        for el in nums:
            counter[el] += 1
        heap = [] # (count, element)
        import heapq
        for key, val in counter.items():
            heapq.heappush(heap, (-1*val, key))
        print(heap)
        ans = set()
        while len(ans) < k:
            el_count, el = heapq.heappop(heap)
            ans.add(el)
        return list(ans)