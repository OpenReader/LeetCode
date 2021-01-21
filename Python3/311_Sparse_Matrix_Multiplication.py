class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def buildMap(M):
            ht = {}
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if M[i][j] != 0:
                        ht[(i,j)] = M[i][j]
            return ht
        
        k, m, n = len(A[0]), len(A), len(B[0])
        # A_map = buildMap(A)
        AB = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                for p in range(k):
                    AB[i][j] += A[i][p] * B[p][j]
        
        return AB