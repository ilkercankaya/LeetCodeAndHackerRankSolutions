import collections

# O(N)
class Solution:
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        freqDic = collections.defaultdict(list)

        for key,value in counter.items():
            freqDic[value].append(key)

        result = []
        for i in range(len(nums),-1,-1):
            if i in freqDic:
                result.extend(freqDic[i])
                if len(result) >= k:
                    return result[:k]
        return result

# import heapq, collections
# # Time complexity O(N * log K + K)
# class Solution:
#     def topKFrequent(self, nums, k):
#         heap = []
#
#         numList = [(freq, num) for num, freq in collections.Counter(nums).items()]
#
#         for num in numList:
#             if len(heap) < k:
#                 heapq.heappush(heap, num)
#             else:
#                 if num > heap[0]:
#                     heapq.heappushpop(heap, num)
#
#
#         return [heapq.heappop(heap)[1] for i in range(k)][::-1]
#
# s = Solution()
# print(s.topKFrequent([1,1,1,2,2,2,2,2,3],2))