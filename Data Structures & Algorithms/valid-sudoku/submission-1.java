class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        for (int row = 0; row < 9; row++) {
            Set<Character> seen_row = new HashSet<>();
            Set<Character> seen_col = new HashSet<>();
            for (int col = 0; col < 9; col++) {
                char row_char = board[row][col];
                char col_char = board[col][row];
                if (row_char != '.' && seen_row.contains(row_char)) {
                    return false;
                }
                if (row_char != '.') {
                    seen_row.add(row_char);
                }

                if (col_char != '.' && seen_col.contains(col_char)) {
                    return false;
                }
                if (col_char != '.') {
                    seen_col.add(col_char);
                }
                
            }
        }

        for (int i = 0; i < 9; i+=3) {
            for (int j = 0; j < 9; j+=3) {
                Set<Character> seen = new HashSet<>();
            
                for (int r = 0; r < 3; r++) {
                    for (int c = 0; c < 3; c++) {
                        char cur_char = board[i + r][j + c];

                        if (cur_char != '.' && seen.contains(cur_char)) {
                            return false;
                        }
                        if (cur_char != '.') {
                            seen.add(cur_char);
                        }
                    }
                }

            }
        }

        return true;
    }
}
