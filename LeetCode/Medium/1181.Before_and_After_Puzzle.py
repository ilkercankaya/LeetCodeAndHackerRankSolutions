import collections


class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        if not phrases:
            return []

        begins = collections.defaultdict(list)

        for i, phrase in enumerate(phrases):
            splitted = phrase.split()
            begins[splitted[0]].append((phrase,i))

        results = set()
        for i, phrase in enumerate(phrases):
            splitted = phrase.split()
            for matchPhrase in begins[splitted[-1]]:
                if i != matchPhrase[1]:
                    results.add(' '.join(splitted + matchPhrase[0].split()[1:]))

        return sorted(list(results))
