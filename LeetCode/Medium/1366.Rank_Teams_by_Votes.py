class Solution:
    def rankTeams(self, votes) -> str:
        if not votes:
            return ""

        teamNum = len(votes[0])

        teamMap = {team: ([0] * teamNum) + [team] for team in votes[0]}

        for vote in votes:
            for rank, team in enumerate(vote):
                teamMap[team][rank] -= 1


        return ''.join(list(map(lambda x: x[-1],sorted(teamMap.values()))))




s = Solution()
print(s.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
print(s.rankTeams(["WXYZ","XYZW"]))
print(s.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
print(s.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))