class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, L = 0, len(nums)
        while i < L:
            while nums[i] > 0 and nums[i] <= L and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            i += 1
        for i in range(L):
            if nums[i] != i+1:
                return i+1
        return L+1