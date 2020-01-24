class Solution:
    def nextGreaterElements(self, nums):
        nums2 = nums * 2

        monotStack = []

        mapper = [-1] * len(nums2)

        for i, num in enumerate(nums2):
            while monotStack and monotStack[-1][0] < num:
                mapper[monotStack.pop()[1]] = num

            monotStack.append((num, i))

        return mapper[:len(mapper) // 2]