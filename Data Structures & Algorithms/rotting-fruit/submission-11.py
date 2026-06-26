class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid),len(grid[0])
        mins = 0
        di = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque()
        def valid(r,c):
            if r>=ROW or c>=COL or r<0 or c<0 or grid[r][c]==0:
                return False
            return True
        fresh = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh +=1
        if fresh ==0:
            return 0
        while q and fresh>0:
            l = len(q)
            for i in range(l):
                r,c = q.popleft()
                for dr,dc in di:
                    if valid(r+dr,c+dc)and grid[r+dr][c+dc]==1:
                        fresh -=1
                        grid[r+dr][c+dc] = 2
                        q.append((dr+r,c+dc))
            mins +=1
        return mins if mins>0 and fresh ==0 else -1


