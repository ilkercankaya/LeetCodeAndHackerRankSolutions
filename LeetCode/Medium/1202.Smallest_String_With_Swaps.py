import collections


class Solution:
    def smallestStringWithSwaps(self, s, pairs) -> str:
        if not s:
            return ""

        # Parent representation of each element in union find
        parents = [- 1] * len(s)

        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                parents[parentX] = parentY

        def find(x):
            if parents[x] == -1:
                return x
            else:
                parents[x] = find(parents[x])
                return parents[x]

        groupsOfPairs = collections.defaultdict(list)

        # Iterate each pair and union them
        for x, y in pairs:
            union(x, y)

        # Group the pairs in a dict
        for i, char in enumerate(s):
            groupsOfPairs[find(i)].append(char)

        # Sort the groups in reverse to later pop
        for values in groupsOfPairs.values():
            values.sort(reverse=True)

        # Merge them back
        results = []

        for i, char in enumerate(s):
            results.append(groupsOfPairs[find(i)].pop())

        return ''.join(results)




