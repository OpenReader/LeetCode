class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(pq, nums[i])
            else:
                heapq.heappushpop(pq, nums[i])
        return pq[0]