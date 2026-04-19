class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW,COL=len(heights),len(heights[0])
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        pac,atl = set(), set()
        def dfs(last, ocean, r, c):
            if r<0 or c<0 or c==COL or r==ROW or heights[r][c]<last or (r,c) in ocean:
                return
            ocean.add((r,c))
            for dr,dc in di:
                dfs(heights[r][c], ocean, dr+r, dc+c)
        for r in range(ROW):          
            dfs(heights[r][0],pac,r,0)
            dfs(heights[r][COL-1],atl,r,COL-1)
        for c in range(COL):
            dfs(heights[0][c],pac,0,c)
            dfs(heights[ROW-1][c],atl,ROW-1,c)
        print(atl)
        print(pac)
        return [list(cell) for cell in pac if cell in atl]
        