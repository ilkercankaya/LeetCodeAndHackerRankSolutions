class Solution:
    def _visitRoom(self, room, roomNum, dic, toBeVisited):
        dic[roomNum] = 1

        for i in range(len(room)):
            toBeVisited.add(room[i])

    def _canVisitAllRooms(self, rooms, dic, toBeVisited):

        while len(toBeVisited) > 0:
            roomNum = toBeVisited.pop()

            # the room is not visited before
            if dic[roomNum] == -1:
                self._visitRoom(rooms[roomNum], roomNum, dic, toBeVisited)

        return not -1 in dic

    def canVisitAllRooms(self, rooms) -> bool:
        # -1 means not visited
        dic = [-1] * len(rooms)

        # zero is visited
        dic[0] = 1

        willVisit = set(rooms[0])
        return self._canVisitAllRooms(rooms, dic, willVisit)


s = Solution()

print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
