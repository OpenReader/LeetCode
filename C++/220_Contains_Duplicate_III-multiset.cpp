class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (nums.size() == 0 || k == 0) return false;
        multiset<long> w;
        w.insert(nums[0]);
        for (int i = 1; i < nums.size(); i++) {
            multiset<long>::iterator low = w.lower_bound(nums[i]);
            multiset<long>::iterator high = w.upper_bound(nums[i]);
            if (low != w.end() && *low == nums[i]) return true;
            if (low != w.begin() && nums[i] - *(--low) <= t) return true;
            if (high != w.end() && *high - nums[i] <= t) return true;
            w.insert(nums[i]);
            if (w.size() > k) w.erase(nums[i-k]);
        }
        return false;
    }
};