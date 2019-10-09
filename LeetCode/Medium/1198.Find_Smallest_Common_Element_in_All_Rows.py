class Solution:
    def smallestCommonElement(self, mat) -> int:
        if not mat:
            return -1

        setLists = [set(el) for el in mat[1:]]

        for testEls in mat[0]:
            flag = False
            for currEl in setLists:
                if testEls not in currEl:
                    flag = True
                    break

            if not flag:
                return testEls

        return -1