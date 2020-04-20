import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = collections.Counter()

        def isValid():
            return len(chars) <= k

        start = 0
        result = 0
        for end, char in enumerate(s):
            chars[char] += 1

            while not isValid():
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    del chars[s[start]]
                start += 1

            result = max(result, end - start + 1)

        return result
