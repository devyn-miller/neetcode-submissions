class Leaderboard:

    def __init__(self):
        self.lb = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.lb[playerId] += score

    def top(self, K: int) -> int:
        if len(self.lb)<1 or K<1:
            return 0
        x=sorted(self.lb.values(),reverse=True)
        return sum(x[:K])

    def reset(self, playerId: int) -> None:
        self.lb[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
