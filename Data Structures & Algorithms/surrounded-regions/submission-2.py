class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROW, COL = len(board),len(board[0])
        di = [[1,0],[0,1],[-1,0],[0,-1]]
        seen = set()

                    

        def dfs(r,c):
            if (r,c) in seen or r<0 or r>= ROW or c<0 or c>= COL or board[r][c]!='O':
                return
            seen.add((r,c))
 
            for dr,dc in di:
                dfs(dr+r,dc+c)
                    

        for r in range(ROW):
            dfs(r,0)
            dfs(r,COL-1)


        for c in range(COL):
            dfs(0,c)
            dfs(ROW-1,c)
        for r in range(1,ROW-1):
            for c in range(1,COL-1):
                if board[r][c] == 'O' and (r,c) not in seen:
                    board[r][c] = 'X'