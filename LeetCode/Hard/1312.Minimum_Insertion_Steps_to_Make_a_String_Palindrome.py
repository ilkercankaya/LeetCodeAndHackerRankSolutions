import functools

class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def helper(start, end):
            if end <= start:
                return 0

            if s[start] == s[end]:
                return helper(start + 1, end - 1)
            else:
                return 1 + min(helper(start, end - 1), helper(start + 1, end))

        return helper(0, len(s) - 1)


s = Solution()
print(s.minInsertions("leetcode"))
