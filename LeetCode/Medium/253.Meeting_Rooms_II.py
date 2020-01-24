import heapq


class Solution(object):

    # Solution 1: Heap
    def minMeetingRooms(self, intervals):
        intervals.sort()

        heap = []

        for start, end in intervals:
            if len(heap) == 0:
                heapq.heappush(heap, (end, start))
            else:
                if start < heap[0][0]:
                    heapq.heappush(heap, (end, start))
                else:
                    heapq.heappushpop(heap, (end, start))

        return len(heap)

    # Solution 2: Two Pointers, TwoArrays
    # def minMeetingRooms(self, intervals):
    #     start_timings = sorted(i[0] for i in intervals)
    #     end_timings = sorted(i[1] for i in intervals)
    #
    #     start = end = 0
    #
    #     usedRooms = 0
    #
    #     while start < len(intervals):
    #         if start_timings[start] >= end_timings[end]:
    #             usedRooms -= 1
    #             end += 1
    #
    #         usedRooms += 1
    #         start += 1
    #
    #     return usedRooms
    
s = Solution()
print(s.minMeetingRooms([[7,10],[2,4]]))