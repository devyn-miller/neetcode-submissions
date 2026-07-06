class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(weight), capacity
        dp = [0]*(M+1)
        for cap in range(M + 1):
            if weight[0]<= cap:
                dp[cap] = (cap // weight[0]) * profit[0]
        for wei in range(1, N):
            cur = [0]*(M+1)
            for cap in range(1, M + 1):
                skip = dp[cap]
                include = 0
                if cap >= weight[wei]:
                    include = profit[wei] + cur[cap - weight[wei]]
                cur[cap] = max(include, skip)
            dp = cur
        return dp[-1]