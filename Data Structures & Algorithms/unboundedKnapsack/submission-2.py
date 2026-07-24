class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0]*(1+capacity)

        
        for w in range(len(weight)):
            cur = [0]*(1+capacity)
            for cap in range(1, capacity + 1):
                skip = dp[cap]
                include = 0
                if cap >= weight[w]:
                    include = profit[w] + cur[cap - weight[w]]
                cur[cap] = max(skip, include)
            dp = cur
        return dp[capacity]
