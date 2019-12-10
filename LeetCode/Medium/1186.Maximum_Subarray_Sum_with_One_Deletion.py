class Solution:
    def maximumSum(self, arr) -> int:
        def forwardArr(arr):
            if not arr:
                return 0

            localMin = arr[0]
            results = [localMin]

            for i in range(1, len(arr)):
                localMin = max(localMin + arr[i], arr[i])
                results.append(localMin)

            return results

        def backwardArr(arr):
            if not arr:
                return 0

            localMin = arr[-1]
            results = [localMin]

            for i in range(len(arr) - 2, -1, -1):
                localMin = max(localMin + arr[i], arr[i])
                results.append(localMin)

            return results[::-1]

        forwardArray = forwardArr(arr)
        backwardArray = backwardArr(arr)

        result = max(forwardArray)

        for i in range(1, len(forwardArray) - 1):
            result = max(result, forwardArray[i - 1] + backwardArray[i + 1])

        return result

