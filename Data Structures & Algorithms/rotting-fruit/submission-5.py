class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        # 0 representing an empty cell
        # 1 representing a fresh fruit
        # 2 representing a rotten fruit
        fresh = 0
        q = deque()
        ti = 0
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1
        if fresh == 0:
            return 0
        while q:
            l = len(q)
            fresh_changed = fresh
            for _ in range(l):
                valid = 4
                r,c = q.popleft()
                for rr, cc in di:
                    dr = rr+r
                    dc = cc+c
                    if dr<0 or dc<0 or dr>= ROW or dc>=COL or grid[dr][dc] == 0:
                        continue    
                        
                    if grid[dr][dc] == 1:
                        q.append((dr,dc))
                        grid[dr][dc] = 2
                        fresh-=1
            if fresh_changed != fresh:
                ti +=1
        if fresh !=0:
            return -1
        return ti