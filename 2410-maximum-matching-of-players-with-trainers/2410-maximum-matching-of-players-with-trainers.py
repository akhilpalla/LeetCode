class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        for j in trainers:
            if players[i] <= j:
                i += 1
                if i == len(players):
                    break
        return i