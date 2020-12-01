class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(left, right, goal_pos):
            pivot = nums[right]
            j = left
            for i in range(left, right):
                if nums[i] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[right], nums[j] = nums[j], nums[right]
            if j == goal_pos:
                return pivot
            elif j < goal_pos:
                return quickSelect(j+1, right, goal_pos) # go right
            
            return quickSelect(left, j-1, goal_pos) # go left
        
        return quickSelect(0, len(nums)-1, k-1)