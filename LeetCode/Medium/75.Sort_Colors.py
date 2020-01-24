class Solution:

    # dutch partitioning problem
    # https://www.youtube.com/watch?v=ER4ivZosqCg
    # Lomuto-Partition solution
    def sortColors(self, nums) -> None:

        pIndex = 0
        pivot = 0
        for i in range(len(nums)):
            if nums[i] <= pivot:
                nums[i], nums[pIndex] = nums[pIndex], nums[i]
                pIndex += 1

        pIndex = len(nums) - 1
        pivot = 2
        for i in reversed(range(len(nums))):
            if nums[i] >= pivot:
                nums[i], nums[pIndex] = nums[pIndex], nums[i]
                pIndex -= 1


