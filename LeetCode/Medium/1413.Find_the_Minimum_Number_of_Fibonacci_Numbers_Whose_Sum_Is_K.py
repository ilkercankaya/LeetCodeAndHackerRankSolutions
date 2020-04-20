class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        fibNums = [1, 1]

        while fibNums[-1] < k:
            fibNums.append(fibNums[-1] + fibNums[-2])

        i = len(fibNums) - 1
        count = 0
        
        while k > 0:
            fib = fibNums[i]
            count += k // fib
            k %= fib

            i -= 1

        return count