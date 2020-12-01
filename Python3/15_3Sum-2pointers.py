class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(i, j, target: int) -> List[int]:
            res = []
            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                else:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
            return res
        
        nums.sort()
        res = []
        
        i = 0
        while i < len(nums) - 2:
            two_res = twoSum(i+1, len(nums)-1, -nums[i])
            for l in two_res:
                res.append([nums[i], l[0], l[1]])
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        
        return res