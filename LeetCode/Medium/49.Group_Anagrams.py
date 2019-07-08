import collections

class Solution:
    def groupAnagrams(self, strs):
        def keyMaker(word):
            numsList = [0] * 26
            for c in word:
                numsList[ord(c) - ord('a')] += 1
            return tuple(numsList)

        dic = collections.defaultdict(list)
        for string in strs:
            dic[keyMaker(string)].append(string)

        return list(dic.values())
