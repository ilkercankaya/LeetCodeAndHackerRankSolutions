import collections

class Solution:
    def groupThePeople(self, groupSizes):

        idMap = collections.defaultdict(list)
        results = []

        for i, size in enumerate(groupSizes):
            idMap[size].append(i)

            if len(idMap[size]) == size:
                results.append(idMap[size])
                idMap[size] = []

        return results