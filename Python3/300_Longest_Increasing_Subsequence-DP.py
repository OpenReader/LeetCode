class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        LIS = [1] * L
        ret = 0
        for i in range(L-1, -1, -1):
            max_lis = 0
            for j in range(i+1, L):
                if nums[j] > nums[i]:
                    max_lis = max(max_lis, LIS[j])
            LIS[i] = max_lis + 1
            ret = max(ret, max_lis + 1)
        return ret