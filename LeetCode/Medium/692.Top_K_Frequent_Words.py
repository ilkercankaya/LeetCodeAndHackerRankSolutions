import collections, heapq


class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.word > other.word


class Solution:

    def topKFrequent(self, words, k):
        minHeap = []

        wordFreqList = [(word, freq) for word, freq in collections.Counter(words).items()]

        for freqWord in wordFreqList:
            if len(minHeap) < k:
                heapq.heappush(minHeap, Word(freqWord[0], freqWord[1]))
            else:
                heapq.heappushpop(minHeap, Word(freqWord[0], freqWord[1]))

        return [i.word for i in [heapq.heappop(minHeap) for i in range(k)][::-1]]
