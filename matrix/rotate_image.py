"""
https://leetcode.com/problems/rotate-image/description/
"""
# TODO look at official solution
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        def rotate_layer(n):
            # rotate layer n in place in 4 steps
            # top to right
            for iter_ in range(n, m-n-1):
                top = matrix[n][iter_]
                right = matrix[iter_][m-1 - n]
                bottom = matrix[m-1 - n][m-1 - iter_]
                left = matrix[m-1 - iter_][n]
                # print(top, right, bottom, left)
                # right -> top
                matrix[iter_][m-n-1] = top
                # bottom -> right
                matrix[m-n-1][m-1 - iter_] = right
                # left -> bottom
                matrix[m-1 - iter_][n] = bottom
                # top gets left
                matrix[n][iter_] = left
        for i in range(m//2):
            rotate_layer(i)