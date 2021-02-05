class Solution {
public:
    string longestPalindrome(string s) {
        int len = 1;
        string ret;
        ret += s[0];
        for (int i = 0; i < s.length() - 1; i++) {
            int j = i + 1;
            while (j < s.length()) {
                if (i * 2 - j >= 0 && s[i * 2 - j] == s[j]) j++;
                else break;
            }
            if (len < 2 * (j - i) - 1) {
                len = 2 * (j - i) - 1;
                ret = s.substr(i * 2 - j + 1, len);
            }
            if (s[i] == s[i+1]) {
                int j = i + 2;
                while (j < s.length()) {
                    if (2 * i - j + 1 >= 0 && s[2 * i - j + 1] == s[j]) j++;
                    else break;
                }
                if (len < 2 * (j - i - 1)) {
                    len = 2 * (j - i - 1);
                    ret = s.substr(i * 2 - j + 2, len);
                }
            }
        }
        return ret;
    }
};