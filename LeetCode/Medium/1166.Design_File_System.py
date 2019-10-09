import collections

class FileSystem:

    def __init__(self):
        self.paths = collections.defaultdict(dict)

    def create(self, path: str, value: int) -> bool:
        parents = path.split("/")[1:]

        accum = ""
        for i in range(len(parents) - 1):
            parent = parents[i]
            accum += parent
            if accum not in self.paths:
                return False

        accum += parents[-1]
        if accum in self.paths:
            return False

        self.paths[accum] = value

        return True

    def get(self, path: str) -> int:
        parents = path.split("/")[1:]

        accum = ""
        for i in range(len(parents)):
            parent = parents[i]
            accum += parent
            if accum not in self.paths:
                return -1

        return self.paths[accum]

fs = FileSystem()
print(fs.create("/a", 1))
print(fs.get("/a"))

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)