class Solution:
    memo = {}
    
    def numSquares(self, n: int) -> int:    
        if n in Solution.memo:
            return Solution.memo[n]
        if n == 0:
            return 0

        i = 1
        min_dep = float('inf')
        while i * i <= n:
            min_dep = min(self.numSquares(n - i * i), min_dep)
            i += 1
        
        Solution.memo[n] = min_dep + 1
        return min_dep + 1