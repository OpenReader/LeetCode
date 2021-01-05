class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        L = len(costs)
        if L == 0: return 0
        K = len(costs[0])
        pre_color, cur_color = -1, -1
        pre_min, pre_sec = 0, 0
        for i in range(L):
            cur_min, cur_sec = float('inf'), float('inf')
            for k in range(K):
                if k == pre_color:
                    cost = pre_sec + costs[i][k]
                else:
                    cost = pre_min + costs[i][k]
                    
                if cost <= cur_min:
                    cur_color = k
                    cur_sec = cur_min
                    cur_min = cost
                elif cost < cur_sec:
                    cur_sec = cost
            # print(cur_min, cur_sec)
            pre_color = cur_color
            pre_min, pre_sec = cur_min, cur_sec

        return cur_min