class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxi=0
        for i in range(len(prices)):
            r=len(prices)-1
            while r > i:
                maxi=max(prices[r] - prices[i],maxi)
                r-=1
        return maxi