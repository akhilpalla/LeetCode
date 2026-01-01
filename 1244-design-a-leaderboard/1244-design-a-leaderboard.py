class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        top_scores = sorted(self.board.values(), reverse=True)
        return sum(top_scores[:K])

    def reset(self, playerId: int) -> None:
        del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)