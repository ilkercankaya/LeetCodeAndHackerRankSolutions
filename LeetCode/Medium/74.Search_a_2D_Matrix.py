class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        index = left - 1

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False