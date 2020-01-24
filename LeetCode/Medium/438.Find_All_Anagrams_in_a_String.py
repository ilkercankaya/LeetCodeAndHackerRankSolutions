from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        cP = Counter(p)
        cS = Counter(s[:len(p) - 1])
        res = []
        for i in range(len(p) - 1, len(s)):
            tailIndex = i - len(p) + 1

            # append head
            cS[s[i]] += 1
            if cS == cP:
                res.append(tailIndex)

            # pop tail
            cS[s[tailIndex]] -= 1

            if cS[s[tailIndex]] == 0:
                del cS[s[tailIndex]]
        return res