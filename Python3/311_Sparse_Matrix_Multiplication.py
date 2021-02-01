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
        A_map = buildMap(A)
        B_col = []
        AB = [[0] * n for _ in range(m)]
        
        for j in range(n):
            for i in range(k):
                if B[i][j] != 0:
                    B_col.append(j)
                    break
        
        for t in A_map:
            for j in B_col:
                    AB[t[0]][j] += A_map[t] * B[t[1]][j]
        
        return AB