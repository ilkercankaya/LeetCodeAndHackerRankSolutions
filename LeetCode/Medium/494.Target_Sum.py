class Solution:
    def helper(self, nums, S, index, memo):

        if index < len(nums):

            key = str(index) + "," + str(S)
            if key not in memo:
                memo[key] = self.helper(nums, S - nums[index], index + 1, memo) + self.helper(
                    nums, S + nums[index], index + 1, memo)

            return memo[key]

        if S == 0:
            return 1
        else:
            return 0

    def findTargetSumWays(self, nums, S):
        memo = {}
        return self.helper(nums, S, 0, memo)


s = Solution()

print(s.findTargetSumWays([1,0], 1))