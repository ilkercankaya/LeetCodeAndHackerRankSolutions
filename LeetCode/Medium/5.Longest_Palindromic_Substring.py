class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        dp = [[True if i == j else False for i in range(len(s))] for j in range(len(s))]

        maxLength = 1
        start = end = 0
        for i in range(len(s) - 1, -1, - 1):
            for j in range(len(s) - 1, i, - 1):
                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                curLen = j - i + 1

                if dp[i][j] and curLen > maxLength:
                    start, end = i, j
                    maxLength = curLen

        return s[start:end + 1]


s = Solution()
print(s.longestPalindrome("cbbd"))