from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s, p = s2, s1

        cP = Counter(p)
        cS = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            tailIndex = i - len(p) + 1

            # append head
            cS[s[i]] += 1
            if cS == cP:
                return True

            # pop tail
            cS[s[tailIndex]] -= 1

            if cS[s[tailIndex]] == 0:
                del cS[s[tailIndex]]
        return False