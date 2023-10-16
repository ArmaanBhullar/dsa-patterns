"""
https://leetcode.com/problems/set-matrix-zeroes/description/
"""
# TODO Look at official solution
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # scan the matrix on mn time and find all rows and columns which should go to zero? Then make them so?
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = []
        zero_cols = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        for row in zero_rows:
            matrix[row] = [0]*n
        for col in zero_cols:
            for i in range(m):
                matrix[i][col] = 0
