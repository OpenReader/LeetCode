class Solution {
public:
    int len;
    
    bool valid(string& num, int start, long fir, long sec) {
        // cout << fir << " " << sec << " " << start << endl;
        string pre_sum = to_string(fir + sec);
        if (start == len) return true;
        if (num.substr(start, pre_sum.size()) == pre_sum) return valid(num, start+pre_sum.size(), sec, fir + sec);
        return false;
    }
    
    bool isAdditiveNumber(string num) {
        len = num.size();
        
        for (int i = 0; i < len / 2; i++) {
            string fir_s = num.substr(0, i+1);
            if (fir_s.size() > 1 && fir_s[0] == '0') continue;
            long fir = stol(fir_s);
            for (int j = 1; j <= len - i -1 && j <= len / 2; j++) {
                string sec_s = num.substr(i+1, j);
                if (sec_s.size() > 1 && sec_s[0] == '0') continue;
                long sec = stol(sec_s);
                // prune
                if (i + j + 1 >= len || to_string(fir + sec).size() > len - (i + j + 1)) break;
                // valid test
                // cout << fir << " " << sec << endl;
                if (valid(num, i + j + 1, fir, sec)) return true;
            }
        }
        
        return false;
    }
};