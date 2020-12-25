class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ret = []
        
        for i in range(k):
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])
        ret.append(dq[0])
        
        L = len(nums)
        for i in range(k, L):
            # clean dq
            if dq and dq[0] == nums[i-k]:
                dq.popleft()
            while dq and dq[-1] < nums[i]:
                dq.pop()
            
            dq.append(nums[i])
            ret.append(dq[0])
        
        return ret