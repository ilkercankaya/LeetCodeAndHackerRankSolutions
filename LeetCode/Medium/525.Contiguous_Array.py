class Solution:
    def findMaxLength(self, nums) -> int:
        balance = 0

        balanceMap = {0: -1}

        res = 0
        for i, num in enumerate(nums):
            balance += 1 if num == 0 else -1

            if balance not in balanceMap:
                balanceMap[balance] = i
            else:
                res = max(res, i - balanceMap[balance])

        return res