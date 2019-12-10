import math


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        l, r = 1, max(nums)

        def check(candidate):
            return sum(math.ceil(num / candidate) for num in nums)

        while l <= r:
            middle = (l + r) // 2

            if check(middle) > threshold:
                l = middle + 1
            else:
                r = middle - 1

        return l
