class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return vector<int> (1, 0);
        unordered_map<int, unordered_set<int>> graph;
        for (auto e : edges) {
            graph[e[0]].insert(e[1]);
            graph[e[1]].insert(e[0]);
        }
        
        int step = 0;
        queue<int> q;
        for (auto item : graph)
            if (item.second.size() == 1) {
                q.push(item.first);
                step++;
            }
        
        while (graph.size() > 2) {
            int next = 0;
            while (step) {
                int cur = q.front();
                q.pop();
                int u;
                for (int nei : graph[cur]) u = nei;
                graph.erase(cur);
                graph[u].erase(cur);
                if (graph[u].size() == 1) {
                    q.push(u);
                    next++;
                }
                step--;
            }
            step = next;
        }
        
        vector<int> ret;
        for (auto item : graph) ret.push_back(item.first);
        return ret;
    }
};