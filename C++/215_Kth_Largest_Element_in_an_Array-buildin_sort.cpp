class Solution {
public:
    static bool compare (int i, int j) { return (i>j); }
    int findKthLargest(vector<int>& nums, int k) {
        nth_element(nums.begin(), nums.begin()+k-1, nums.end(), compare);
        return nums[k-1];
    }
};