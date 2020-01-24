from collections import defaultdict


class Solution:
    def groupStrings(self, strings):

        results = []

        totalCharNumber = ord("z") - ord("a") + 1
        if not strings:
            return results

        hashmap = defaultdict(list)

        for string in strings:
            offset = ord(string[0]) - ord("a")

            key = []
            for char in string:
                mappedChar = ord(char) - ord("a")
                key.append((mappedChar - offset) % totalCharNumber)

            hashmap[tuple(key)].append(string)

        return hashmap.values()


s = Solution()
print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
