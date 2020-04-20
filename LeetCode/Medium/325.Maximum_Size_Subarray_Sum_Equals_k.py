class Solution:
    def maxSubArrayLen(self, nums, k: int) -> int:
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        indexMapper = {}

        res = 0
        for i, num in enumerate(prefix):
            complement = num - k
            if complement in indexMapper:
                res = max(res, i - indexMapper[complement])

            if num not in indexMapper:
                indexMapper[num] = i
        return res