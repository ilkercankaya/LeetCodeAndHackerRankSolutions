class Solution:
    def minTaps(self, n: int, ranges) -> int:
        max_range = [0] * (n + 1)

        # store the max possible watering to right side of the taps
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            max_range[left] = max(max_range[left], right - left)

        farthestPossible = jumps = endRN = 0
        for i in range(len(max_range) - 1):
            farthestPossible = max(farthestPossible, i + max_range[i])
            # cases when we can not jump further
            if i == farthestPossible:
                return -1

            # all candidates are considered, time for a new turn
            if i == endRN:
                jumps += 1
                endRN = farthestPossible

        return jumps
