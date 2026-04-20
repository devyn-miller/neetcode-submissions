class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sys.setrecursionlimit(3000)
        ROW, COL = len(grid),len(grid[0])
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        self.max_size = 0
        def dfs(r,c):
            if r<0 or c<0 or r>= ROW or c>=COL or grid[r][c]!=1:
                return 0
            grid[r][c] = 0
            area = 1+sum(dfs(r+dr,c+dc) for dr,dc in di)
            self.max_size = max(self.max_size,area)
            return area
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c)
        return self.max_size