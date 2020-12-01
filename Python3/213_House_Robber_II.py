class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(n):
            rob = n[0]
            nrob = 0
            for money in n[1:]:
                tmp = nrob
                # if not rob
                nrob = max(rob, nrob)
                # if rob
                rob = tmp + money
                
            return max(rob, nrob)
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(helper(nums[1:]), helper(nums[:-1]))