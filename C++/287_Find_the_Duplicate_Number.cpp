class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int tortoise = nums[0], hare = nums[0];
        while (true) {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
            if (tortoise == hare) break;
        }
        hare = nums[0];
        while (hare != tortoise) {
            hare = nums[hare];
            tortoise = nums[tortoise];
        }
        return hare;
    }
};