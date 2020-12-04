class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        for i in range(L-1, -1, -1):
            if i == 0:
                break
            if nums[i] > nums[i-1]:
                for j in range(i, L):
                    if nums[j] <= nums[i-1]:
                        break
                    p = j
                nums[i-1], nums[p] = nums[p], nums[i-1]
                break
                
        for j in range(0, (L - i) // 2):
                nums[i+j], nums[L-j-1] = nums[L-j-1], nums[i+j]
        
        return