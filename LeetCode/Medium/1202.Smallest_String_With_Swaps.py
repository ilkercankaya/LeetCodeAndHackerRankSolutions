import collections


class Solution:
    def smallestStringWithSwaps(self, s, pairs) -> str:
        if not s:
            return ""

        # Parent representation of each element in union find
        parents = [- 1] * len(s)

        def find(x):
            if parents[x] < 0:
                return x

            parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            smallRoot, bigRoot = find(x), find(y)

            if smallRoot == bigRoot:
                return

            if abs(parents[smallRoot]) > abs(parents[bigRoot]):
                smallRoot, bigRoot = bigRoot, smallRoot

            if abs(parents[bigRoot]) == abs(parents[smallRoot]):
                parents[bigRoot] -= 1

            parents[smallRoot] = bigRoot

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