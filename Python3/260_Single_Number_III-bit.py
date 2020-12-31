class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        # diff = a ^ b
        for n in nums:
            diff ^= n
        # rightmost 1 bit in diff
        r_diff = diff & (-diff)
        
        a = 0
        for n in nums:
            if r_diff & n: # will not include b
                a ^= n
        
        return [a, diff ^ a]