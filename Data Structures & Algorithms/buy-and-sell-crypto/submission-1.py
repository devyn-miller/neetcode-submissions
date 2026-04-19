class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        mi = float('inf')
        for i in range(len(prices)):
            m = max(m, prices[i] - mi)
            mi = min(mi,prices[i])
        return m
            
