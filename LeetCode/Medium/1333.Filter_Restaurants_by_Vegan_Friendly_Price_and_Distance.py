class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
    List[int]:
        return map(lambda x: x[0], sorted(
            filter(lambda x: (veganFriendly == 0 or x[2] == veganFriendly) and x[3] <= maxPrice and x[4] <= maxDistance,
                   restaurants), key=lambda x: (x[1], x[0]), reverse=True))

