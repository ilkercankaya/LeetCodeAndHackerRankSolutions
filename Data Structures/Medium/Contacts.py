#!/bin/python3

import os
import sys


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        self.total = 0
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            pCrawl.total += 1

            # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return 0
            pCrawl = pCrawl.children[index]

        return pCrawl.total

    #
# Complete the contacts function below.
#
def contacts(queries):
    trie = Trie()
    results = []
    for i in range(len(queries)):
        queryList = queries[i]

        if queryList[0] == "add":
            trie.insert(queryList[1])
        else:

            results.append(trie.search(queryList[1]))

    return results


if __name__ == '__main__':

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    print(result)