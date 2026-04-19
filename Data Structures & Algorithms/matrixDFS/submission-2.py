class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid),len(grid[0])
        if ROW == 1 and COL == 1:
            return 1 if grid[0][0]==0 else 0
        seen = set()
        di=[(0,1),(1,0),(-1,0),(0,-1)]
        self.count = 0
        def dfs(r,c):
            if r>=ROW or c>=COL or r<0 or c<0 or grid[r][c]!=0 or (r,c) in seen:
                return False
            seen.add((r,c))
            for dr,dc in di:
                if dfs(dr+r,dc+c):
                    if dr+r == ROW - 1 and dc+c == COL-1:
                        self.count += 1
            seen.remove((r,c))
            return True
        dfs(0,0)
        return self.count