from collections import defaultdict


class HitCounter:

    def __init__(self):
        self.counter = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        result = 0
        for i in range(timestamp - 300 + 1, timestamp + 1):
            result += self.counter[i]

        return result

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)