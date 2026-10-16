class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen_row = set()
            seen_col = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in seen_row:
                    return False
                elif board[i][j] != ".":
                    seen_row.add(board[i][j])

                if board[j][i] in seen_col:
                    return False
                elif board[j][i] != ".":
                    seen_col.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[k+i][l+j] != "." and board[k+i][l+j] in seen:
                            return False
                        elif board[k+i][l+j] != ".":
                            seen.add(board[k+i][l+j])

        return True