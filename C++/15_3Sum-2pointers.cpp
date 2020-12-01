class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int len = nums.size();
        if(len < 3) return res;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < len-2; i++){
            int target = -nums[i];
            int front = i+1;
            int back = len-1;
            while(front < back){
                int sum = nums[front] + nums[back];
                if(sum > target) back--;
                else if(sum < target) front++;
                else{
                    res.push_back({-target, nums[front], nums[back]});
                    while(nums[++front] == nums[front-1] && front < back) ;
                    while(nums[--back] == nums[back+1] && front < back) ;
                }
            }
            while(i+1 < len-2 && nums[i+1] == nums[i]) i++;
        }
        return res;
    }
};