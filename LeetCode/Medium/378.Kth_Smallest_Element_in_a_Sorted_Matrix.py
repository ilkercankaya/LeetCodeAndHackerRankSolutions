class Solution:
    def kthSmallest(self, matrix, k) -> int:
       OneDMatrix = []
       for i in range(len(matrix)):
           OneDMatrix.extend(matrix[i])

       OneDMatrix.sort()
       return OneDMatrix[k-1]
