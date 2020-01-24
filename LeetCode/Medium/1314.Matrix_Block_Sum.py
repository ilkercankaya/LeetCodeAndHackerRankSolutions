class Solution:
    def matrixBlockSum(self, mat, K):
        prefixMatrix = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]

        directions = [(0, -1), (-1, 0)]
        for i in range(1, len(prefixMatrix)):
            for j in range(1, len(prefixMatrix[i])):
                for xInc, yInc in directions:
                    newX, newY = i + xInc, j + yInc
                    prefixMatrix[i][j] += prefixMatrix[newX][newY]

                prefixMatrix[i][j] += mat[i - 1][j - 1] - prefixMatrix[i - 1][j - 1]


        results = [[0] * len(mat[0]) for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[i])):

                rightDownX = min(i + K, len(mat) - 1) + 1
                rightDownY = min(j + K, len(mat[0]) - 1) + 1

                rightDownSum = prefixMatrix[rightDownX][rightDownY]

                leftUpX = max(0, i - K) + 1
                leftUpY = max(0, j - K) + 1

                rightDownSum -= prefixMatrix[leftUpX - 1][rightDownY]
                rightDownSum -= prefixMatrix[rightDownX][leftUpY - 1]

                results[i][j] = rightDownSum + prefixMatrix[leftUpX - 1][leftUpY - 1]

        return results

s = Solution()
print(s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],1))
print(s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],2))