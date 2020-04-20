import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        def isValid(sCtr, tCtr):
            for key, val in tCtr.items():
                if sCtr[key] < tCtr[key]:
                    return False

            return True

        maxIndexes = (0, float("inf"))

        leftPtr = 0
        tCtr = collections.Counter(t)
        sCtr = collections.Counter()

        for end, char in enumerate(s):
            sCtr[char] += 1

            while isValid(sCtr, tCtr) and end >= leftPtr:
                maxIndexes = min(maxIndexes, (leftPtr, end), key=lambda x: x[1]-x[0])
                sCtr[s[leftPtr]] -= 1
                leftPtr += 1

        return s[maxIndexes[0]:maxIndexes[1] + 1
        if maxIndexes[1] != float("inf") else 0]

s = Solution()
print(s.minWindow("a","a"))

s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))