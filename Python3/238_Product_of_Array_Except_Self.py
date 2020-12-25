class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        output = [1] * L
        # product of all the prefix
        for i in range(1, L):
            output[i] = output[i-1] * nums[i-1]
        
        suffix_p = 1
        for i in range(L-1, -1, -1):
            output[i] *= suffix_p
            suffix_p *= nums[i]
        
        return output