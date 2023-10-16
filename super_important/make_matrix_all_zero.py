"""
https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/description/
"""
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        line_1 = grid[0]
        line_1_complement = [(x+1)%2 for x in line_1]
        for i in range(m):
            if grid[i] != line_1 and grid[i] != line_1_complement:
                return False
        return True