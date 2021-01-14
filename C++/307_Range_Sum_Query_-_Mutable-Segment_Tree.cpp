class NumArray {
private:
    int * tree;
    int n;
public:
    NumArray(vector<int>& nums) {
        if (nums.size()) {
            n = nums.size();
            tree = new int[n * 2];
            for (int i = n, j = 0; i < 2 * n; i++, j++)
                tree[i] = nums[j];
            for (int i = n - 1; i > 0; i--)
                tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }
    }
    
    void update(int index, int val) {
        tree[n + index] = val;
        int i = (n + index) / 2;
        while (i) {
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
            i /= 2;
        }
    }
    
    int sumRange(int left, int right) {
        left += n;
        right += n;
        int sum = 0;
        while (left <= right) {
            if (left % 2 == 1) sum += tree[left++];
            if (right % 2 == 0) sum += tree[right--];
            left /= 2;
            right /= 2;
        }
        return sum;
    }
};