"""
https://leetcode.com/problems/palindromic-substrings/description/
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[None for i in range(n)] for j in range(n)]
        def is_palindrome(left: int, right: int) -> bool :
            if dp[left][right] is None:
                if left >= right:
                    dp[left][right] = True
                # compute and set it
                else:
                    if s[left] != s[right]:
                        dp[left][right] = False
                    else:
                        dp[left][right] = is_palindrome(left + 1, right - 1)
            return dp[left][right]
        summer = 0
        for i in range(n):
            for j in range(i, n):
                ans = int(is_palindrome(i, j))
                # print(i, j, ans)
                summer += ans
        # print(dp)
        return summer