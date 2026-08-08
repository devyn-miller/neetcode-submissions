class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        s = [-1]
        res = [len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            while s and heights[i] > heights[s[-1]]:
                s.pop()
            if not s:
                res.append(i)
            s.append(i)
        return res[::-1]
