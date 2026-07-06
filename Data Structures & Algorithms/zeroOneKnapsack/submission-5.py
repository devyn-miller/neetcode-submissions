class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0]*(capacity + 1)
        for cap in range(capacity+1):
            if weight[0]<=cap:
                dp[cap] = profit[0]
        for w in range(1, len(weight)):
            cur = [0]*(capacity + 1)
            for cap in range(1, capacity + 1):
                skip = dp[cap]
                include = 0
                if cap >= weight[w]:
                    include = profit[w] + dp[cap - weight[w]]
                cur[cap] = max(include, skip)
            dp = cur
        return dp[capacity]
