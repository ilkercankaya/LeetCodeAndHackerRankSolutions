import collections, copy

# Very Inefficient Algorithm - For learning purpose Only!!!

class Solution(object):
    def _helperTile(self, initialString, dict, set):
        for key in dict:
            tileCopy = copy.deepcopy(dict)
            tileCopy[key] -= 1
            if tileCopy[key] == 0:
                del tileCopy[key]

            set.add(initialString + key)
            self._helperTile(initialString + key, tileCopy, set)

    def numTilePossibilities(self, tiles):
        tilesDict = collections.Counter(tiles)
        s = set()
        self._helperTile("", tilesDict, s)

        return len(s)


s = Solution()
print(s.numTilePossibilities("AAABBC"))
