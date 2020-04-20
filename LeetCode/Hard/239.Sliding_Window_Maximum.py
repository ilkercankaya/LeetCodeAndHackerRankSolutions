import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        monotonicQueue = collections.deque()

        for i in range(k):
            num = nums[i]
            while len(monotonicQueue) > 0 and num > monotonicQueue[-1]:
                monotonicQueue.pop()
            monotonicQueue.append(num)

        res = [monotonicQueue[0]]

        for i in range(k, len(nums)):
            num = nums[i]

            if nums[i - k] == monotonicQueue[0]:
                monotonicQueue.popleft()

            while len(monotonicQueue) > 0 and num > monotonicQueue[-1]:
                monotonicQueue.pop()
            monotonicQueue.append(num)

            res.append(monotonicQueue[0])

        return res
