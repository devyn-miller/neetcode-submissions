class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        dp = [[0]*(capacity + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0
        for c in range(capacity + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]
        for item in range(1, n):
            for cap in range(capacity + 1):
                skip = dp[item - 1][cap]
                include = 0
                if cap >= weight[item]:
                    include = dp[item - 1][cap - weight[item]] + profit[item]
                dp[item][cap] = max(skip, include)
        return dp[-1][-1]