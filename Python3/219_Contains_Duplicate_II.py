class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_see = {}
        
        for i in range(len(nums)):
            if nums[i] in last_see:
                if i - last_see[nums[i]] <= k:
                    return True
            last_see[nums[i]] = i
            
        return False