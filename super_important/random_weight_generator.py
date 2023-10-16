"""
https://leetcode.com/problems/random-pick-with-weight/description/
"""
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(self.w)
        self.intervals = []
        summer = 0
        for weight in self.w:
            summer += weight
            self.intervals.append(summer / self.total)

    def pickIndex(self) -> int:
        # generate a random number between 0 and 1,
        x = random.random()
        return self.searchIndex(x, self.intervals)

    def searchIndex(self, x: float, ls: List[float]) -> int:
        # return idx where x >= ls[idx] and x < ls[idx+1]
        n = len(ls)
        left, right = 0, n - 1
        mid = (left + right) // 2
        while right - left > 1:
            if x > ls[mid]:
                left = mid
            elif x < ls[mid]:
                right = mid
            else:
                return mid
            mid = (left + right) // 2
        if ls[left] < x:
            return right
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()