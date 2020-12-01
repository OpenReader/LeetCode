class Solution
    def threeSum(self, nums List[int]) - List[List[int]]
        if len(nums)  3
            return []
        ret = []
        i = 0
        nums.sort()
        print(nums)
        while i  len(nums)-2
            if nums[i]  0
                break
            h = set()
            goal = -nums[i]
            h.add(nums[i+1])
            j = i+2
            while j  len(nums)
                if goal - nums[j] in h
                    ret.append([-goal, goal-nums[j], nums[j]])
                    while j+1  len(nums) and nums[j+1] == nums[j]
                        j += 1
                h.add(nums[j])
                j += 1

            while i+1  len(nums)-2 and nums[i+1] == nums[i]
                i += 1
            i += 1
        
        return ret