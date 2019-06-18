# beats https://leetcode.com/problems/climbing-stairs/

class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        elif n < 3:
            self.cache[n] = n
            return n
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        self.cache[n] = result

        return result
