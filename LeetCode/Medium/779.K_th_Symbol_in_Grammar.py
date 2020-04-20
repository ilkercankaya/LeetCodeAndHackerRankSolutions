class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def kthZeroIndex(N, K):
            if N == 0:
                return 0

            half = 2 ** (N - 1) - 1
            if K <= half:
                return kthZeroIndex(N - 1, K)
            else:
                if kthZeroIndex(N - 1, K - half - 1):
                    return 0
                else:
                    return 1

        return kthZeroIndex(N - 1, K - 1)
