class Solution:
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        opt = [0] * (n + 1)
        max_v, topleft = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                top = opt[j]
                opt[j] = 0
                if matrix[i-1][j-1] == '1':
                    v = min([top, opt[j-1], topleft]) + 1
                    opt[j] = v
                    max_v = max(v, max_v)
                topleft = top
                
        return max_v * max_v