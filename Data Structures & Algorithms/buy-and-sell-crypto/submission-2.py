class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        mi = prices[0]
        for i in range(1, len(prices)):
            re = prices[i] - mi
            if prices[i] < mi:
                mi = prices[i]
            if re > max_diff:
                max_diff=re
        return max_diff
            