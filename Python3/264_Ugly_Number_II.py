class UglyNumber:
    def __init__(self):
        self.nums = [1, ]
        i2 = i3 = i5 = 0
        
        for _ in range(1689):
            ugly = min(self.nums[i2] * 2, self.nums[i3] * 3, self.nums[i5] * 5)
            self.nums.append(ugly)
            if self.nums[i2] * 2 == ugly:
                i2 += 1
            if self.nums[i3] * 3 == ugly:
                i3 += 1
            if self.nums[i5] * 5 == ugly:
                i5 += 1

class Solution:
    u = UglyNumber()
    def nthUglyNumber(self, n: int) -> int:
        print(self.u.nums)
        return self.u.nums[n - 1]