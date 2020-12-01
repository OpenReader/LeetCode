class Solution {
public:
    void swap(vector<int>& nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
    int partition(vector<int>& nums, int l, int r) {
        int pivot = nums[l];
        int p = l;
        while (l < r) {
            if (nums[r] < pivot) {
                r--;
                continue;
            }
            if (nums[l] >= pivot) {
                l++;
                continue;
            }
            swap(nums, l, r);
        }
        swap(nums, l, p);
        return l;
    }
    int findKthLargest(vector<int>& nums, int k) {
        int l = 0, r = nums.size() - 1;
        while (true) {
            int m = partition(nums, l, r);
            if (m == k - 1) return nums[m];
            else if (m > k - 1) r = m - 1;
            else l = m + 1;
        }
        return -1;
    }
};