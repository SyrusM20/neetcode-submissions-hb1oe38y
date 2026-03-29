class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        dp = [[False] * n  for _ in range(n)]
        best_start, best_len = 0, 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    curr_len = j - i + 1
                    if curr_len > best_len:
                        best_len = curr_len
                        best_start = i
        return s[best_start: best_start + best_len]