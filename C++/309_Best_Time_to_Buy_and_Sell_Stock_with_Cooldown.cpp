class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int held = INT_MIN, sold = INT_MIN, reset = 0;
        for (int price: prices) {
            int sold_i = held + price;
            held = max(reset - price, held);
            reset = max(reset, sold);
            sold = sold_i;
        }
        return max(sold, reset);
    }
};