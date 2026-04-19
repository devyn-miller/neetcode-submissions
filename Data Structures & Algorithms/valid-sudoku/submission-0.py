class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                # if board[i][j] in rows[i] or board[j][i] in cols[i] or board[i][j] in boxes[i]:
                #     return False
                
                if board[i][j] in rows[i]:
                    print('rows')
                    return False
                rows[i].add(board[i][j])
                
                if board[i][j] in cols[j]:
                    print('cols')
                    return False
                cols[j].add(board[i][j])
                
                
                if board[i][j] in  boxes[i//3,j//3]:
                    return False
                boxes[i//3,j//3].add(board[i][j])

        return True

