class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        def robNonCircular(nums):

            last, now = 0, 0

            for i in nums:
                last, now = now, max(last + i, now)

            return now

        return max(robNonCircular(nums[:-1]), robNonCircular(nums[1:]))