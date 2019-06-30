# Biweekly Contest 3

class Solution:
    def maximumMinimumPath(self, A):
        if len(A) == 0:
            return 0

        rows = len(A)
        columns = len(A[0])

        pathList = []
        pathMap = [[0 for x in range(columns)] for y in range(rows)]

        travelStack = [(0, 0)]

        while travelStack:
            i, j = travelStack.pop()
            pathList.append(A[i][j])
            pathMap[i][j] = 1
            neighbours = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
            neighbourList = []
            flag = False
            for k in range(len(neighbours)):
                x = neighbours[k][0]
                y = neighbours[k][1]
                if x == rows - 1 and y == columns - 1:
                    travelStack.clear()
                    flag = True
                    pathList.append(A[x][y])
                    break
                if not (x < 0 or y < 0 or x >= rows or y >= columns or pathMap[x][y] == 1):
                    neighbourList.append((A[x][y], x, y))

            if flag:
                break

            maxEl = max(neighbourList)
            travelStack.append((maxEl[1], maxEl[2]))

        return min(pathList)


s = Solution()
# print(s.maximumMinimumPath([[0,1,0,0,1],[1,1,0,0,0],[1,0,1,1,1],[1,0,1,0,1],[1,0,1,0,1]]))
print(s.maximumMinimumPath([[2, 0, 2, 3, 1], [0, 2, 2, 3, 3], [2, 3, 0, 2, 3], [1, 1, 2, 3, 1], [2, 2, 0, 0, 1]]))
