class Solution {
public:
    int reverse(int x) {
        int ret = 0;
        int pre_max = INT_MAX / 10;
        int pre_min = -1 * pre_max;
        while (x != 0) {
            int digit = x % 10;
            x /= 10;
            if (ret > pre_max || ret == pre_max && digit > 7) return 0;
            if (ret < pre_min || ret == pre_min && digit < -8) return 0;
            ret = ret * 10 + digit;
        }
        return ret;
    }
};