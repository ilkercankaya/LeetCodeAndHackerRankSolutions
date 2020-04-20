class Solution:
    # Time complexity: O(N logN)
    # Space complexity: O(1)
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0

        points.sort()

        minEnd = float("inf")
        arrowsShot = 0

        for point in points:
            if point[0] > minEnd:
                arrowsShot += 1
                minEnd = point[1]
            else:
                minEnd = min(minEnd, point[1])

        return arrowsShot + 1

# Time complexity: O(N logN)
# Space complexity: O(N)

# import heapq
# class Solution:
#     def findMinArrowShots(self, points) -> int:
#         if not points:
#             return 0
#
#         points.sort()
#
#         pq = []
#         arrowsShot = 0
#
#         for point in points:
#             if len(pq) > 0 and point[0] > pq[0]:
#                 pq = []
#                 arrowsShot += 1
#
#             heapq.heappush(pq, point[1])
#
#         return arrowsShot + 1