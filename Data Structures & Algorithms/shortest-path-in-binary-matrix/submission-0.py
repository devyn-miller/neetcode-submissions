class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]!=0:
            return -1
        ROW,COL = len(grid),len(grid)
        q = deque()
        q.append([(0,0)])
        di = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        def valid(r,c):
            if (r,c) in vi or r<0 or r>=ROW or c<0 or c>=COL or grid[r][c]!=0:
                return False
            return True
        dim = len(grid)
        ct = 1
        vi = set((0,0))
        while q:
            n = q.popleft()
            size = len(n)
            t = []
            for v in range(size):
                r, c = n[v]
                if r == len(grid)-1 and c == len(grid)-1:
                    return ct
                for dr,dc in di:
                    if valid(dr+r,dc+c):
                        t.append((dr+r,dc+c))
                        vi.add((dr+r,dc+c))
            if t:
                q.append(t)
                ct +=1
        return -1
            



