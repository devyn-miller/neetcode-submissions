class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0]*(capacity + 1)
        for w in range(len(weight)):
            cur = [0]*(capacity + 1)
            for cap in range(capacity + 1):
                skip = dp[cap]
                include = 0
                if cap - weight[w] >= 0:
                    include = profit[w] + dp[cap - weight[w]]
                cur[cap] = max(skip,include)
            dp = cur
        return dp[capacity]
