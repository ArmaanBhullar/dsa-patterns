"""
https://leetcode.com/problems/spiral-matrix/description/
"""
# TODO look at official solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        ls = []

        def print_matrix_layer(row_start, row_end, col_start, col_end):
            # print(row_start, row_end, col_start, col_end)
            # print first row
            for col in range(col_start, col_end + 1):
                ls.append(matrix[row_start][col])
            # print last column
            for row in range(row_start + 1, row_end + 1):
                ls.append(matrix[row][col_end])

            if row_start != row_end:
                # print last row in reverse
                for col in range(col_end - 1, col_start - 1, -1):
                    ls.append(matrix[row_end][col])
            if col_start != col_end:
                # print first column
                for row in range(row_end - 1, row_start, -1):
                    ls.append(matrix[row][col_start])

        for i in range((min(m, n) + 1) // 2):
            print_matrix_layer(i, m - i - 1, i, n - i - 1)

        return ls