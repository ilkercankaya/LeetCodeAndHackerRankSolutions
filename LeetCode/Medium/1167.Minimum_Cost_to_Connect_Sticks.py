import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        heap = sticks
        cost = 0

        if len(heap) < 2:
            return sum(heap)

        while len(heap) != 1:
            smallestOne = heapq.heappop(heap)
            smallestTwo = heapq.heappop(heap)

            sumSmallestTwo = smallestOne + smallestTwo
            cost += sumSmallestTwo
            heapq.heappush(heap, sumSmallestTwo)

        return cost