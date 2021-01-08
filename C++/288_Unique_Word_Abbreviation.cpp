class ValidWordAbbr {
public:
    unordered_map<string, unordered_set<string>> record;
    
    string getAbbr(string s) {
        int l = s.size();
        if (l < 3) return s;
        return s[0]+to_string(l-2)+s[l-1];
    }
    
    ValidWordAbbr(vector<string>& dictionary) {
        for (string s: dictionary) record[getAbbr(s)].insert(s);
    }
    
    bool isUnique(string word) {
        string abbr = getAbbr(word);
        if (!record.count(abbr)) return true;
        if (record[abbr].count(word) && record[abbr].size() == 1) return true;
        return false;
    }
};