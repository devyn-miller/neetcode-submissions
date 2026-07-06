class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        dp_last = [0]*(capacity + 1)
        for c in range(capacity + 1):
            if weight[0] <= c:
                dp_last[c] = profit[0]
        for item in range(1, n):
            dp_curr = [0]*(capacity + 1)
            for cap in range(1, capacity + 1):
                skip = dp_last[cap]
                include = 0
                if cap >= weight[item]:
                    include = dp_last[cap - weight[item]] + profit[item]
                dp_curr[cap] = max(skip, include)
            dp_last = dp_curr
        return max(dp_last)