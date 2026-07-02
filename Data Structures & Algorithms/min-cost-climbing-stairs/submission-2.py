class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost[0]<cost[1]:
            for i in range(2,len(cost)):
                cost[i] += min(cost[i-2],cost[i-1])
        else:
            cost[2] += cost[1]
            for i in range(3,len(cost)):
                cost[i] += min(cost[i-2],cost[i-1])
        return min(cost[-1],cost[-2])