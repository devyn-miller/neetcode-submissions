class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid),len(grid[0])
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        m = 0
        def dfs(r,c):
            if r<0 or c<0 or c>=COL or r>=ROW or grid[r][c]!=1:
                return
            grid[r][c] = 0
            size[0]+=1
            for dr,dc in di:
                dfs(dr+r,dc+c)
        for r in range(ROW):
            for c in range(COL):
                size = [0]
                dfs(r,c)
                m = max(m, size[0])
        return m

            
