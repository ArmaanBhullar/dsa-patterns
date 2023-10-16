"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
"""
class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        # This one uses DP to calculate what's the largest square size that ends at an element on matrix
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # extend diagonal value if above and below are atleast equal to the diagonal value
                    dp[i][j] = min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) + 1
        return sum([sum(dp[i]) for i in range(m)])

    def countSquaresn_n_n(self, matrix: List[List[int]]) -> int:
        # let k = min(m, n)
        # count all mutually exclusive blocks of size 1..k
        # apply formula - size k bloack has 1^2 + .. k^2 squares
        m = len(matrix)
        n = len(matrix[0])
        self.counter = 0
        square_size_count = defaultdict(int)
        visited = [[0 for i in range(n)] for j in range(m)]

        # print(len(visited), len(visited[0]))
        def start_search(x: int, y: int) -> int:
            max_size = 1
            while (1):

                # print(x, y, max_size)
                for row in range(x, x + max_size):
                    if matrix[row][y + max_size - 1] == 0:
                        return max_size - 1
                for col in range(y, y + max_size):
                    if matrix[x + max_size - 1][col] == 0:
                        return max_size - 1
                # boundary check returns only once previous has been confirmed
                if x + max_size == m or y + max_size == n:
                    return max_size
                max_size += 1

        # greedily mark squares as visited and of the maxiumum size
        counter = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    max_size = start_search(i, j)
                    # mark as visited
                    for x in range(i, i + max_size):
                        for y in range(j, j + max_size):
                            visited[x][y] = 1
                    # print(i, j, max_size)
                    self.counter += max_size
        return self.counter