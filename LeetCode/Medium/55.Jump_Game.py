class Solution:
    def canJump(self, nums) -> bool:
        maxSoFar = 0
        for i in range(len(nums)):
            if i > maxSoFar or maxSoFar > len(nums) - 1:
                break

            maxSoFar = max(maxSoFar, i + nums[i])

        return maxSoFar >= len(nums) - 1



