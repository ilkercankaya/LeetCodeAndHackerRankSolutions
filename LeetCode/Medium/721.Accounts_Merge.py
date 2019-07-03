import collections


class Solution:
    def accountsMerge(self, accounts):

        parents = [i for i in range(1000000)]

        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
                return parents[a]
            else:
                return a

        def union(a, b):
            aRoot = find(a)
            bRoot = find(b)

            if aRoot != bRoot:
                parents[bRoot] = aRoot

        emToID = {}
        emToName = {}

        id = 0
        for acc in accounts:
            for email in acc[1:]:
                emToName[email] = acc[0]

                if email not in emToID:
                    emToID[email] = id
                    id += 1

                union(emToID[email], emToID[acc[1]])

        merged = collections.defaultdict(list)

        for email in emToName:
            merged[find(emToID[email])].append(email)

        return [[emToName[v[0]]] + sorted(v) for v in merged.values()]
