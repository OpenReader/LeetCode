class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []
        for n in nums:
            i = bisect_right(piles, n)
            if i-1 >= 0 and piles[i-1] == n:
                continue
            if i == len(piles):
                piles.append(n)
            else:
                piles[i] = n
        return len(piles)