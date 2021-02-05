class Solution {
public:
    string convert(string s, int numRows) {
        
        if (numRows == 1) return s;
        
        vector<string> zig (min(int(s.size()), numRows));
        int cyc = 2 * numRows - 2;
        for (int i = 0; i < s.size(); i++) {
            int index = i % cyc;
            if (index < numRows) zig[index] += s[i];
            else zig[cyc - index] += s[i];
        }
        string ret;
        for (string sub: zig) ret += sub;
        return ret;
    }
};