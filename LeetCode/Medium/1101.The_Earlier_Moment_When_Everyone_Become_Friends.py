class Solution:
    def earliestAcq(self, logs, N):
        logs.sort(key=lambda x: x[0])
        friendsList = [[i] for i in range(N)]

        for log in logs:

            indexI = None
            indexJ = None
            for it ,list in enumerate(friendsList):
                i = it if log[1] in list else None
                j = it if log[2] in list else None

                if i is not None:
                    indexI = i

                if j is not None:
                    indexJ = j

                if indexI is not None and indexJ is not None:
                    break

            if indexI != indexJ:
                mergesList = friendsList[indexI] + friendsList[indexJ]
                one = friendsList[indexI]
                two = friendsList[indexJ]
                friendsList.remove(one)
                friendsList.remove(two)
                friendsList.append(mergesList)

            if len(friendsList) == 1:
                return log[0]

        if len(friendsList) != 1:
            return -1


s = Solution()
print(s.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]],6))
