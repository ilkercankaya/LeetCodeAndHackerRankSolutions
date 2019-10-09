class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return nums

        results = [1] * len(nums)

        for i in range(1, len(nums)):
            results[i] = results[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(len(nums))):
            results[i] = results[i] * R
            R *= nums[i]

        return results

