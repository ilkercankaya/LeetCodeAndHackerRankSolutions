class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        curr = nums[0]
        shiftBy = 0
        count = 1
        for id in range(1, len(nums)):
            num = nums[id]

            if count - 2 > 0 and curr != num:
                shiftBy += count - 2

            nums[id - shiftBy] = nums[id]

            if curr == num:
                count += 1
            elif curr != num:
                curr = num
                count = 1

        if count - 2 > 0:
            shiftBy += count - 2

        for i in range(shiftBy):
            nums.pop()

        return len(nums)