# Iterative version
# def myPow(x, n):
#     """
#     :type x: float
#     :type n: int
#     :rtype: float
#     """
#     if n < 0:
#         x = 1 / x
#         n = -n
#     result = 1
#     while n:
#         if n % 2:
#             result *= x
#         x *= x
#         n = n // 2
#     return result

# Recursive
class Solution:
    def _power(self, x, n, result = 1):
        # result = 1
        # while n:
        #     if n % 2:
        #         result *= x
        #     x *= x
        #     n = n//2
        if n % 2:
            return self._power(x * x, n // 2, result * x)
        elif n == 0:
            return result
        else:
            return self._power(x * x, n // 2, result)

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        return self._power(x, n)

sol = Solution()
print(sol.myPow(3,6))