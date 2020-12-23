class Solution:
    # solution's code
    def majorityElement(self, nums):
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result

    # my code
    def myMajorityElement(self, nums: List[int]) -> List[int]:
        L = len(nums)
        
        ret = []
        fir, sec = None, None
        fir_cnt, sec_cnt = 0, 0
        # first pass
        i = 0
        while i < L:
            if nums[i] != fir and nums[i] != sec:
                fir_cnt -= 1
                sec_cnt -= 1
                if fir_cnt < 0 and sec_cnt < 0:
                    fir_cnt, sec_cnt = 0, 0
                    fir = nums[i]
                    while i < L and nums[i] == fir:
                        i += 1
                        fir_cnt += 1
                    if i < L:
                        sec = nums[i]
                        sec_cnt += 1
                elif fir_cnt < 0:
                    fir = nums[i]
                    fir_cnt = 1
                    sec_cnt += 1
                elif sec_cnt < 0:
                    sec = nums[i]
                    sec_cnt = 1
                    fir_cnt += 1
            elif nums[i] == fir:
                fir_cnt += 1
            elif nums[i] == sec:
                sec_cnt += 1
            i += 1
        # second pass
        fir_cnt, sec_cnt = 0, 0
        for n in nums:
            if n == fir:
                fir_cnt += 1
            elif n == sec:
                sec_cnt += 1
        
        if fir_cnt > L//3:
            ret.append(fir)
        if sec_cnt > L//3:
            ret.append(sec)
        return ret