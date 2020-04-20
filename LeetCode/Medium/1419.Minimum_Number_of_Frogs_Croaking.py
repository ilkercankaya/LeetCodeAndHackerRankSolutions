class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:


        mapper = {"c": 0, "r": 1, "o":2, "a":3, "k":4}
        charNums = [0,0,0,0,0]

        frogs = 0
        res = 0
        for char in croakOfFrogs:
            if char == "c":
                frogs += 1
            elif char == "k":
                frogs -= 1

            charNums[mapper[char]] += 1

            for char in ["c","r","o","a"]:
                if charNums[mapper[char]] < charNums[mapper[char] + 1]:
                    return -1

            res = max(res, frogs)

        return res if all([num == charNums[0] for num in charNums]) else -1