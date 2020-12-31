# opt[i+1][0] = min(opt[i][1], opt[i][2]) + costs[i+1][0] 
# opt[i+1][1] = min(opt[i][0], opt[i][2]) + costs[i+1][1]
# opt[i+1][2] = min(opt[i][0], opt[i][1]) + costs[i+1][2] 

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        L = len(costs)
        
        for i in range(1, L):
            for a in range(3):
                b, c = (a + 1) % 3, (a + 2) % 3
                costs[i][a] += min(costs[i-1][b], costs[i-1][c])
        
        return 0 if L == 0 else min(costs[L-1])