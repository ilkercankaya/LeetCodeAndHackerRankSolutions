class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        initSum = sum(arr[:k])

        threshold *= k

        result = 0
        result += int(initSum >= threshold)

        for i in range(k, len(arr)):
            initSum += arr[i] - arr[i - k]
            result += int(initSum >= threshold)

        return result
    
