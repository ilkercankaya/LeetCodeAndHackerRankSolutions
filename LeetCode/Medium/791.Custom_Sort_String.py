import collections

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        idCounter = 0
        dic = collections.defaultdict(int)

        for char in S:
            dic[char] = idCounter
            idCounter += 1

        return ''.join(sorted(T, key=lambda x: dic[x]))