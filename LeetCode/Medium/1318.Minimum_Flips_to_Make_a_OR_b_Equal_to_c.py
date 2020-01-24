class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        binA = '{:032b}'.format(a)
        binB = '{:032b}'.format(b)
        binC = '{:032b}'.format(c)

        sumRes = 0
        for i, char in enumerate(binC):
            if char == "0":
                sumRes += sum([int(digit == "1") for digit in [binA[i], binB[i]]])
            else:
                sumRes += int(not(binA[i] == "1" or binB[i] == "1"))


        return sumRes