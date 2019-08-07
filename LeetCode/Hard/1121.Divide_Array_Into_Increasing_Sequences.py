import collections


class Solution:
    def canDivideIntoSubsequences(self, nums, K: int) -> bool:
        return max(collections.Counter(nums).values()) * K <= len(nums)
