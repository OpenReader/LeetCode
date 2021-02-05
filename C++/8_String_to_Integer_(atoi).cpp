class Solution {
public:
    int myAtoi(string s) {
        if (s.size() == 0) return 0;
        long ret = 0;
        int i = 0;
        // leading whitespace
        while (s[i] == ' ') i++;
        // '+' or '-'
        int sign = 1;
        if (s[i] == '+') i++;
        else if (s[i] == '-') {
            sign = -1;
            i++;
        }
        // digits
        while (s[i] >= '0' && s[i] <= '9') {
            ret = ret * 10 + (s[i++] - '0');
            if (sign == 1 && ret >= INT_MAX) return INT_MAX;
            if (sign == -1 && ret > INT_MAX) return INT_MIN;
        }
        return (int)ret * sign;
    }
};