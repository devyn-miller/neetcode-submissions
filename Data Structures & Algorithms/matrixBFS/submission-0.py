class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid),len(grid[0])
        di = [[0,1],[0,-1],[-1,0],[1,0]]
        q = deque()
        q.append((0,0,0))
        visited = set()
        while q:
            r,c,l = q.popleft()
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for dr,dc in di:
                if dr+r<ROW and dc+c<COL and dr+r>=0 and dc+c>=0 and grid[r][c]==0:
                    q.append((dr+r,dc+c,l+1))
            if r==ROW-1 and c==COL-1:
                return l
        return -1

