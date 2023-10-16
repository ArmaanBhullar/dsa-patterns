"""
https://leetcode.com/problems/find-median-from-data-stream/description/
"""
class MedianFinder:
    # maintain two heaps - lo and hi, invariant is size(lo) - size(hi) = 0 or 1
    # max(lo) <= min(hi)
    # balance when adding new element
    def __init__(self):
        self.lo = [] # min heap so store -1* element
        self.hi = []

    def balance(self):
        # only for imbalance of 1 element
        if len(self.lo) - len(self.hi) > 1:
            el = -1*heapq.heappop(self.lo)
            heapq.heappush(self.hi, el)
        elif len(self.lo) - len(self.hi) in [0, 1]:
            # do nothing
            pass
        else:
            el = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -1*el)

    def addNum(self, num: int) -> None:
        if len(self.lo) == 0:
            heapq.heappush(self.lo, -1*num)
        else:
            if (len(self.hi) > 0) and (num >= self.hi[0]):
                # put in hi
                heapq.heappush(self.hi, num)
            elif num <= -1*self.lo[0]:
                heapq.heappush(self.lo, -1*num)
            else:
                # send to maintain size invariant
                if len(self.lo) > len(self.hi):
                    heapq.heappush(self.hi, num)
                else:
                    heapq.heappush(self.lo, -1*num)
            # done adding the numbder, now balance
        self.balance()

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-1*self.lo[0] + self.hi[0])/2
        else:
            return -1*self.lo[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()