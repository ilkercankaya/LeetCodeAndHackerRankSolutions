import math


class Solution:
    def kClosest(self, points, K):
        return [num[1] for num in
                sorted(list(zip([math.sqrt(math.pow(x, 2) + math.pow(y, 2)) for x, y in points], points)))[:K]]
