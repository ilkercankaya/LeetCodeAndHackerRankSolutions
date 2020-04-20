import collections


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        reversedDic = collections.defaultdict(set)

        for row, col in reservedSeats:
            reversedDic[row].add(col)

        totalFam = 0
        for key, reversedSet in reversedDic.items():
            regions = [1, 1, 1]
            if 2 in reversedSet or 3 in reversedSet:
                regions[0] = 0
            if 4 in reversedSet or 5 in reversedSet:
                regions[0] = 0
                regions[1] = 0
            if 6 in reversedSet or 7 in reversedSet:
                regions[1] = 0
                regions[2] = 0
            if 8 in reversedSet or 9 in reversedSet:
                regions[2] = 0

            if all(regions):
                totalFam += 2
            elif any(regions):
                totalFam += 1

        return totalFam + 2 * (n - len(reversedDic))