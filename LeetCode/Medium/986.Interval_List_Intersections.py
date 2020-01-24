class Solution:
    def intervalIntersection(self, A, B):
        intersections = []

        i = j = 0

        while i < len(A) and j < len(B):
            intersectX = max(A[i][0], B[j][0])
            intersectY = min(A[i][1], B[j][1])

            if intersectX <= intersectY:
                intersections.append([intersectX, intersectY])

            if intersectY == B[j][1]:
                j += 1
            else:
                i += 1

        return intersections
