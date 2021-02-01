class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        vector<int> ret;
        for (int i = 0; i < nums.size(); i++) {
            if (seen.count(target - nums[i])) {
                ret.push_back(i);
                ret.push_back(seen[target - nums[i]]);
            }
            else seen[nums[i]] = i;
        }
        return ret;
    }
};