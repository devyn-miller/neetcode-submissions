class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW,COL = len(grid),len(grid[0])
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            r,c = q.popleft()
            dist = grid[r][c]
            # if grid[r][c]==2147483647 and dist!=0:
            #     grid[r][c] = dist
            for dr,dc in di:
                if dr+r < 0 or dc+c < 0 or dr+r >=ROW or dc+c>=COL or grid[r+dr][c+dc]!=2147483647:
                    continue
                q.append((dr+r,dc+c))
                grid[dr+r][c+dc] = dist + 1




