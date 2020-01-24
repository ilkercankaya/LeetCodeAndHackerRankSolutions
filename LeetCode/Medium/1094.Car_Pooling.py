class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        l = []

        for cost, start, end in trips:
            l.append((start, cost))
            l.append((end, -cost))

        l.sort()

        curCap = 0
        for timeFrame, cost in l:
            curCap += cost
            if curCap > capacity:
                return False

        return True
