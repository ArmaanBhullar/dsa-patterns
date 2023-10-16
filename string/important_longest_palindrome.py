"""
https://leetcode.com/problems/longest-palindromic-substring/description/
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None for i in range(n)] for j in range(n)]

        # calculate dp stepwise then iterate and find the answer
        def is_palindrome(left: int, right: int) -> bool:

            if dp[left][right] is None:
                # calculate the answer
                if left >= right:
                    dp[left][right] = True
                elif s[left] == s[right]:
                    dp[left][right] = is_palindrome(left + 1, right - 1)
                else:
                    dp[left][right] = False
                    # print(left, right, s[left:right+1], dp[left][right])
            return dp[left][right]

        for i in range(n):
            for j in range(i + 1):
                # print(i, j)
                if is_palindrome(j, n - i + j - 1):
                    return s[j: n - i + j]
        return ""