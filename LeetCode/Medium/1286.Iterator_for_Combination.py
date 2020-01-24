from itertools import combinations
from collections import deque
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = deque(combinations(characters, combinationLength))

    def next(self) -> str:
        return ''.join(self.combinations.popleft())

    def hasNext(self) -> bool:
        return len(self.combinations) != 0