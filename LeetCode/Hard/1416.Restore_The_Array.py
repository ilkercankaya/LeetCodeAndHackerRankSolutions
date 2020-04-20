class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        dp = [0] * (len(s) + 1)

        kLen = len(str(k))

        for i in reversed(range(len(s))):
            if s[i] == "0":
                dp[i] = 0
                continue

            if len(s) - i <= kLen and int(s[i:]) <= k:
                dp[i] = 1

            for j in range(i, min(len(s), i + 1 + kLen)):
                if int(s[i:j + 1]) <= k:
                    dp[i] += dp[j + 1]

        return dp[0] % 1000000007

