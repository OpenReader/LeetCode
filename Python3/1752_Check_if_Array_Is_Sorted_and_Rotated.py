class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        start = 0
        min_ele = 101
        for i, n in enumerate(nums):
            if n < min_ele:
                min_ele = n
                start = i
        if start == 0:
            i = N - 1
            while i >= 0 and nums[i] == min_ele:
                i -= 1
            start = i + 1
        
        pre = 0
        for i in range(N):
            if nums[(start + i) % N] >= pre:
                pre = nums[(start + i) % N]
            else:
                return False
        return True