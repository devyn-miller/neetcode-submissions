class Solution:
    def maxArea(self, heights: List[int]) -> int:

        re=0
        l = 0
        r=len(heights)-1
        while l<r:
            print((r-l) * (min(heights[l],heights[r])))
            if ((r-l) * (min(heights[l],heights[r]))) > re:
                re=((r-l) * (min(heights[l],heights[r])))
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return re
            