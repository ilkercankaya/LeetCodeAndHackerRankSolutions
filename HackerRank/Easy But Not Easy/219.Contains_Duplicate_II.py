# Beats 97.45%, all written by me from scratch
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dicNum = {}

        for id, num in enumerate(nums):
            if num in dicNum:
                if id - dicNum[num] <= k:
                    return True
                dicNum[num] = max(dicNum[num], id)
            else:
                dicNum[num] = id

        return False


# Even more optimal - Not by me
# class Solution:
#     def containsNearbyDuplicate(self, nums, k: int) -> bool:
#         dicNum = {}
#
#         for id, num in enumerate(nums):
#             if num in dicNum:
#                 if id - dicNum[num] <= k:
#                     return True
#             dicNum[num] = id
#
#         return False
