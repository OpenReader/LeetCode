class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}
        
        def getBucketId(n):
            return n // (t+1)
        
        for i in range(len(nums)):
            # print(buckets)
            b_id = getBucketId(nums[i])
            if b_id in buckets:
                return True
            if b_id-1 in buckets and nums[i] - buckets[b_id-1] <= t:
                return True
            if b_id+1 in buckets and buckets[b_id+1] - nums[i] <= t:
                return True
            buckets[b_id] = nums[i]
            if i >= k:
                buckets.pop(getBucketId(nums[i-k]))
                
        return False