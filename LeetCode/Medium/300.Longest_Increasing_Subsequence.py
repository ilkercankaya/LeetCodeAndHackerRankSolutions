class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)

        for i in range(1,len(nums)):
            maxSoFar = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxSoFar = max(maxSoFar, dp[j])

            dp[i] = max(dp[i], dp[i] + maxSoFar)

        return max(dp)