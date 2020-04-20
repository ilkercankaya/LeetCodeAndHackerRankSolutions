class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2 ** (n - 1):
            return ""

        div = 2 ** (n - 1)

        mapper = {"a": "bc", "b": "ac", "c": "ab"}

        res = []

        def helper(n, k, prev):
            nonlocal div
            div //= 2
            if n == 0:
                return

            index = k // div
            cur = mapper[prev][index]
            res.append(cur)
            helper(n - 1, k % div, cur)

        k -= 1
        firstStr = chr(ord('a') + (k // div))
        res.append(firstStr)
        helper(n - 1, k % div, firstStr)

        return "".join(res)
