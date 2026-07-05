class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        di = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def dfs(r,c, i, ocean):
            if r<0 or c<0 or r==ROW or c==COL or (r,c) in ocean or heights[r][c]<i:
                return
            ocean.add((r,c))
            res.append((r,c))
            for dr, dc in di:
                dfs(dr + r, dc + c, heights[r][c], ocean)
        pac = set()
        atl = set()
        for r in range(ROW):
            res = []
            dfs(r,0, -1, set())
            pac.update(set(res))
            res = []
            dfs(r,COL-1, -1, set())
            atl.update(set(res))
        for c in range(COL):
            res = []
            dfs(0,c, -1, set())
            pac.update(set(res))
            res = []
            dfs(ROW-1,c, -1, set())
            atl.update(set(res))
        atl = set(atl)
        pac = set(pac)
        return list(pac.intersection(atl))
