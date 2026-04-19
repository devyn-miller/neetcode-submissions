class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=0
        # for i in range(len(heights)):
        r=len(heights)-1
        l=0
        while r > l:
            length = r-l
            prod = length*min(heights[l],heights[r])
            print(length, min(heights[l],heights[r]),prod)
            maxi=max(maxi,prod)
            if heights[l]>heights[r]:
                r-=1
            else: l+=1
        
            
        return maxi