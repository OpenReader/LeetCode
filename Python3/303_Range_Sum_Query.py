class NumArray:

    def __init__(self, nums: List[int]):
        self.acc = nums.copy()
        for i in range(1, len(nums)):
            self.acc[i] += self.acc[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.acc[j] if i == 0 else self.acc[j] - self.acc[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)