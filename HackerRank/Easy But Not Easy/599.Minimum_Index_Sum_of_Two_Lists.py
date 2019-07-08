import collections
class Solution:
    def findRestaurant(self, list1, list2):
        dicOne = {}
        for id, rest in enumerate(list1):
            dicOne[rest] = id

        dicTwo = {}
        for id, rest in enumerate(list2):
            dicTwo[rest] = id

        commonSumToRestName = collections.defaultdict(list)

        for key in dicOne:
            if key in dicTwo:
                commonSumToRestName[dicOne[key] + dicTwo[key]].append(key)

        for i in range(len(list1) + len(list2)):
            if i in commonSumToRestName:
                return commonSumToRestName[i]