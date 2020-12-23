class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        L = len(nums)
        if L == 0:
            return []
        
        ret = []
        pre = start = nums[0]
        for n in nums[1:]:
            if n != pre + 1:
                if pre == start:
                    ret.append(str(pre))
                else:
                    ret.append(str(start)+"->"+str(pre))
                start = n
            pre = n
        
        if pre == start:
            ret.append(str(pre))
        else:
            ret.append(str(start)+"->"+str(pre))
            
        return ret