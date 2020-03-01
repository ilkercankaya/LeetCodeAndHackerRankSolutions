import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = collections.Counter(s)
        tCount = collections.Counter(t)

        res = 0
        for char, key in sCount.items():
            res += abs(tCount[char] - key)

        for char, key in tCount.items():
            if char not in sCount:
                res += tCount[char]

        return res // 2


s = Solution()
print(s.minSteps("acd","xmn"))
print(s.minSteps("aacd","axmn"))
print(s.minSteps("aacyd","axemn"))
print(s.minSteps("leetcode", "practice"))
print(s.minSteps("anagram", "mangaar"))