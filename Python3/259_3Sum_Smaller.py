class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        L = len(nums)
        if L < 3:
            return 0
        ret= 0
        nums.sort()
        for i in range(L-2):
            i_target = target - nums[i]
            lo, hi = i + 1, L - 1
            while lo < hi:
                if nums[lo] + nums[hi] >= i_target:
                    hi -= 1
                else:
                    ret += hi - lo
                    lo += 1
        
        return ret