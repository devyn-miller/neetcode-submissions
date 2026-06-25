class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def valid(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL:
                return False
            return True
        ROW,COL=len(grid),len(grid[0])
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([[r,c]])
        print(q)
        while q:
            n = q.popleft()
            temp = []
            
            for i in range(len(n)):
                
                r,c = n[i][0],n[i][1]
                if not valid(r,c):
                    continue
                m = 2147483647
                for dr,dc in di:
                    if not valid(r+dr,c+dc):
                        continue
                    if grid[r+dr][c+dc] == 2147483647:
                        temp.append([r+dr,c+dc])
                        grid[r+dr][c+dc] = min(m, grid[r][c]+1)
            if temp:
                q.append(temp)
                    


            