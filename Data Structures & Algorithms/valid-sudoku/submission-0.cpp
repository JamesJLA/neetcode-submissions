class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < board.size(); i++) {
            // set for row
            unordered_set<char> seen_row;
            // set for column
            unordered_set<char> seen_column;            
            for (int j = 0; j < board[i].size(); j++) {
                // goes over the row first need to keep track of column as well
                if (seen_row.contains(board[i][j])) {
                    return false;
                } else if (!(seen_row.contains(board[i][j])) && !(board[i][j] == '.')){
                    seen_row.insert(board[i][j]);
                }

                if (seen_column.contains(board[j][i])) {
                    return false;
                } else if (!(seen_column.contains(board[j][i])) && !(board[j][i] == '.')) {
                    seen_column.insert(board[j][i]);
                }
            }
        }

        for (int row_box = 0; row_box < 9; row_box+=3) {
            for (int col_box = 0; col_box < 9; col_box+=3) {
                unordered_set<char> box_seen;
                for (int row = 0; row < 3; row++) {
                    for (int col = 0; col < 3; col++) {
                        if (box_seen.contains(board[row+row_box][col+col_box])) {
                    return false;
                } else if (!(box_seen.contains(board[row+row_box][col+col_box])) && !(board[row+row_box][col+col_box] == '.')){
                    box_seen.insert(board[row+row_box][col+col_box]);
                }
                    }
                }
            }
        }

        return true;

    }
};
