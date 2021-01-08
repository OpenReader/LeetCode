class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = 0;
        int L = nums.size();
        for (; j < L; j++) {
            if (nums[j] != 0)
                nums[i++] = nums[j];
        }
        while (i < L) nums[i++] = 0;
        return;
    }
};