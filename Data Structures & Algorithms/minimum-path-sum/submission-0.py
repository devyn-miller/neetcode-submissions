class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        for r in range(1, ROW):
            grid[r][0] += grid[r - 1][0]
        for c in range(1, COL):
            grid[0][c] += grid[0][c - 1]
        for r in range(1, ROW):
            for c in range(1, COL):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]