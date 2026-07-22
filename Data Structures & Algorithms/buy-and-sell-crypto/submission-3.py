class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        res = 0
        for p in prices:
            if p < mi:
                mi = p
            if p > mi:
                res = max(res, p - mi)
        return res