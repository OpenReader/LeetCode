class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int m = rooms.size(), n = rooms[0].size();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    // bfs
                    queue<pair<int, int>> q;
                    q.push(make_pair(i, j));
                    while (!q.empty()) {
                        pair<int, int> cur = q.front();
                        int cur_i = cur.first, cur_j = cur.second, cur_val = rooms[cur_i][cur_j];
                        q.pop();
                        // up
                        if (cur_i - 1 >= 0 && rooms[cur_i-1][cur_j] > cur_val + 1) {
                            rooms[cur_i-1][cur_j] = cur_val + 1;
                            q.push(make_pair(cur_i-1, cur_j));
                        }
                        // down
                        if (cur_i + 1 < m && rooms[cur_i+1][cur_j] > cur_val + 1) {
                            rooms[cur_i+1][cur_j] = cur_val + 1;
                            q.push(make_pair(cur_i+1, cur_j));
                        }
                        // left
                        if (cur_j - 1 >= 0 && rooms[cur_i][cur_j-1] > cur_val + 1) {
                            rooms[cur_i][cur_j-1] = cur_val + 1;
                            q.push(make_pair(cur_i, cur_j-1));
                        }
                        // ringt
                        if (cur_j + 1 < n && rooms[cur_i][cur_j+1] > cur_val + 1) {
                            rooms[cur_i][cur_j+1] = cur_val + 1;
                            q.push(make_pair(cur_i, cur_j+1));
                        }
                    }
                }
            }
        return;
    }
};