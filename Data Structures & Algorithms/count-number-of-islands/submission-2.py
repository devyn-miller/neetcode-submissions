class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        di = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            if c<0 or c==COL or r<0 or r== ROW or grid[r][c] == '0':
                return
            grid[r][c]='0'
            for dr,dc in di:
                dfs(r+dr,c+dc)
        ct=0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    dfs(r,c)   
                    ct +=1 
        return ct
            