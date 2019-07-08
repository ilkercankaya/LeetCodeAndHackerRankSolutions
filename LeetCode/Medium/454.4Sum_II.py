import collections
class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        count = 0

        dicAB = collections.defaultdict(int)
        for aNum in A:
            for bNum in B:
                dicAB[aNum+bNum] += 1

        for cNum in C:
            for dNum in D:
                count += dicAB[-cNum-dNum]

        return count
