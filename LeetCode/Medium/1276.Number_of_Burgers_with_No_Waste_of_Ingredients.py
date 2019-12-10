class Solution:

    # O(log N)
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):
        if tomatoSlices < cheeseSlices * 2:
            return []
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]

        l, r = 0, cheeseSlices

        while l <= r:
            middle = l + (r - l) // 2
            numOfJumbo = cheeseSlices - middle
            
            currTomatoSlices = middle * 2 + numOfJumbo * 4

            if currTomatoSlices > tomatoSlices:
                l = middle + 1
            elif currTomatoSlices < tomatoSlices:
                r = middle - 1
            else:
                return [numOfJumbo, middle]

        return []

    # # O(N)
    # def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):
    #
    #     if tomatoSlices < cheeseSlices * 2:
    #         return []
    #     if tomatoSlices == 0 and cheeseSlices == 0:
    #         return [0, 0]
    #
    #     # incrementally check if a burger can be constructed
    #     for i in range(cheeseSlices + 1):
    #         # i is the number of small burgers
    #         numOfJumboBurgers = cheeseSlices - i
    #
    #         if i * 2 + numOfJumboBurgers * 4 == tomatoSlices:
    #             return [numOfJumboBurgers, i]
    #
    #     return []

s = Solution()
print(s.numOfBurgers(4,2))