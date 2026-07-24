class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for i in range(capacity + 1):
            if weight[0] <= i:
                dp[i] = profit[0]
        for i in range(1, len(weight)):
            cur = [0] * (capacity + 1)
            for j in range(1, capacity + 1):
                skip = dp[j]
                include = 0
                if weight[i] <= j:
                    include = dp[j-weight[i]] + profit[i]
                cur[j] = max(skip,include)
            dp = cur
        return dp[capacity]
