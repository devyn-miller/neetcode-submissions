class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0
        for i in range(len(heights)):
            l=i
            r=len(heights)-1
            while r > l:
                length = r-l
                prod = length*min(heights[l],heights[r])
                print(length, min(heights[l],heights[r]),prod)
                maxi=max(maxi,prod)
                r-=1
            
            
        return maxi