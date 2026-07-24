class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0]*(1+capacity)
        for w in range(len(weight)):
            cur = [0]*(1+capacity)
            for c in range(capacity + 1):
                skip = dp[c]
                include = 0
                if weight[w]<=c:
                    include = profit[w] + cur[c - weight[w]]
                cur[c] = max(skip, include)
            dp = cur
        return dp[capacity]