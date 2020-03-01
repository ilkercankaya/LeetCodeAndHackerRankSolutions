import math
class Solution:
    def closestDivisors(self, num: int):
        upperBound = int(math.sqrt(num + 2))

        for i in reversed(range(upperBound + 1)):
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]
            elif (num + 2) % i == 0:
                return [i, (num + 2) // i]

s = Solution()
print(s.closestDivisors(8))
print(s.closestDivisors(123))
print(s.closestDivisors(999))