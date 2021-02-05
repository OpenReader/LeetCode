class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ret = 0;
        int low = 0;
        unordered_map<char, int> index_of;
        for (int i = 0; i < s.length(); i++) {
            if (index_of.count(s[i]) && index_of[s[i]]>= low) {
                ret = i - low > ret ? i - low : ret;
                low = index_of[s[i]] + 1;
            }
            index_of[s[i]] = i;
        }
        return s.length() - low > ret ? s.length() - low : ret;
    }
};