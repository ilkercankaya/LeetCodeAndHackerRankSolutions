# passes https://leetcode.com/problems/fibonacci-number/

class Solution:
    cache = {}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]

        if N < 2:
            self.cache[N] = N
            return N

        result = self.fib(N - 1) + self.fib(N - 2)

        self.cache[N] = result

        return result