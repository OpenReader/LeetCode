class UnionFind {
private:
    vector<int> parent;
    vector<int> rank;
    int count;
public:
    UnionFind (int size) {
        parent = vector<int> (size, -1);
        rank = vector<int> (size, 0);
        count = 0;
    }
    
    void setParent (int i) {
        if (parent[i] != -1) return; 
        parent[i] = i;
        count++;
    }
    
    bool exist (int i) {
        return parent[i] == -1 ? false : true;
    }
    
    int getCount() {
        return count;
    }
    
    int find (int i) {
        if (parent[i] != i) parent[i] = find(parent[i]);
        return parent[i];
    }
    
    void Union (int a, int b) {
        int roota = find(a);
        int rootb = find(b);
        if (roota == rootb) return;
        count--;
        if (rank[roota] > rank[rootb])
            parent[rootb] = roota;
        else if (rank[roota] < rank[rootb])
            parent[roota] = rootb;
        else {
            rank[rootb] += 1;
            parent[roota] = rootb;
        }
    }
    
    // void printState() {
    //     for (int i : parent) cout << i << " ";
    //     cout << endl;
    //     for (int i : rank) cout << i << " ";
    //     cout << endl;
    //     cout << "-------------" << endl;
    // }
};

class Solution {
public:
    vector<int> numIslands2 (int m, int n, vector<vector<int>>& positions) {
        UnionFind lands (m * n);
        vector<int> ret;
        
        for (auto pos: positions) {
            int x = pos[0], y = pos[1];
            lands.setParent(x * n + y);
            if (x - 1 >= 0 && lands.exist((x - 1) * n + y)) lands.Union(x * n + y, (x - 1) * n + y);
            if (x + 1 < m && lands.exist((x + 1) * n + y)) lands.Union(x * n + y, (x + 1) * n + y);
            if (y - 1 >= 0 && lands.exist(x * n + y - 1)) lands.Union(x * n + y, x * n + y - 1);
            if (y + 1 < n && lands.exist(x * n + y + 1)) lands.Union(x * n + y, x * n + y + 1);
            ret.push_back(lands.getCount());
            // lands.printState();
        }
        
        return ret;
    }
};