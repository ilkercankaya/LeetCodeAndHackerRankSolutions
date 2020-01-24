class Solution:

    #O(d * target) solution
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dp(d, target):
            if target <= 0:
                return 0

            if d == 1:
                return 1 if 1 <= target <= f else 0

            if (d, target) in memo:
                return memo[(d, target)]

            res = dp(d, target - 1) + dp(d - 1, target - 1)

            memo[(d, target)] = res
            if target - f - 1 >= 0:
                memo[(d, target)] -= dp(d - 1, target - f - 1)

            return memo[(d, target)]

        return dp(d, target) % (10 ** 9 + 7)

    # # O(d * f * target) solution
    # def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    #     memo = {}
    #
    #     def dp(d, target):
    #         if d == 1:
    #             return 1 if 1 <= target <= f else 0
    #
    #         if (d, target) in memo:
    #             return memo[(d, target)]
    #
    #         res = 0
    #         for i in range(1, f + 1):
    #             res += dp(d - 1, target - i)
    #
    #         memo[(d,target)] = res
    #         return res
    #
    #     return dp(d, target) % (10 ** 9 + 7)
