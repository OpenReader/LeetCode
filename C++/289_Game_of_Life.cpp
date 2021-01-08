class Solution {
public:
    int m;
    int n;
    vector<vector<int>> dirs = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    
    int getLiveNei(vector<vector<int>>& board, int i, int j) {
        int ret = 0;
        for (vector<int> d : dirs) {
            if (i+d[0] < m && i+d[0] >= 0 && j+d[1] < n && j+d[1] >= 0 && (board[i+d[0]][j+d[1]] == 1 || board[i+d[0]][j+d[1]] == 3))
                ret++;
        }
        return ret;
    }
    
    void gameOfLife(vector<vector<int>>& board) {
        // 0->1: 2; 1->0: 3
        m = board.size(), n = board[0].size();
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) {
            int live_nei = getLiveNei(board, i, j);
            if (board[i][j] == 1 && (live_nei < 2 || live_nei > 3)) // live cell
                board[i][j] = 3;
            else if (board[i][j] == 0 && live_nei == 3) // dead cell
                board[i][j] = 2;
        }

        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) {
            if (board[i][j] == 2) board[i][j] = 1;
            else if (board[i][j] == 3) board[i][j] = 0;
        }
        return;
    }
};