class Solution:

    # Time: O(N)
    def numTimesAllBlue(self, light) -> int:
        candidate = 0
        total = 0
        for i, num in enumerate(light):
            if num > candidate:
                candidate = num

            if i == candidate - 1:
                total += 1

        return total

    # Time(N logN)
    # def numTimesAllBlue(self, light) -> int:
    #     import heapq
    #     top = 0
    #     heap = []
    #
    #     moments = 0
    #     for num in light:
    #         if num - 1 == top:
    #             top = num
    #         else:
    #             heapq.heappush(heap, num)
    #
    #         while len(heap) > 0 and heap[0] - 1 == top:
    #             top = heapq.heappop(heap)
    #
    #         if len(heap) == 0:
    #             moments += 1
    #
    #     return moments