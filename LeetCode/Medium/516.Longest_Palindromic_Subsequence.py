import functools
class Solution:
    def longestPalindromeSubseq(self, s) -> int:
        @functools.lru_cache(None)
        def helper(start, end):
            if start == end:
                return 1
            if start > end:
                return 0

            if s[start] == s[end]:
                return 2 + helper(start + 1, end - 1)
            else:
                return max(helper(start, end - 1), helper(start + 1, end))

        return helper(0, len(s) - 1)

s = Solution()
print(s.longestPalindromeSubseq("cbbd"))
