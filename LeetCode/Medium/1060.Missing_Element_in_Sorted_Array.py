class Solution:
    def missingElement(self, nums, k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx

        left, right = 0, len(nums)

        while left < right:
            pivot = left + (right - left) // 2

            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot

        return nums[left - 1] + k - missing(left - 1)

