class Solution:
    def jump(self, nums):
        farthestPossible = jumps = endRN = 0

        for i in range(len(nums) - 1):
            farthestPossible = max(farthestPossible, i + nums[i])
            if i == endRN:
                jumps += 1
                endRN = farthestPossible


        return jumps


# Solution 2 - Not concise
# class Solution:
#     def jump(self, nums) -> int:
#         if len(nums) <= 1:
#             return 0
#
#         maxSoFar, jumps = nums[0], 1
#         currentIndex = 0
#         while currentIndex <= len(nums) - 1:
#             prev = maxSoFar
#             for i in range(currentIndex, maxSoFar + 1):
#                 if i == len(nums) - 1:
#                     return jumps
#                 maxSoFar = max(maxSoFar, i + nums[i])
#
#             currentIndex = prev + 1
#             jumps += 1
#
#         return jumps