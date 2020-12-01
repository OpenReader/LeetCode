class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        
        def backtracking(start_num, c_sum, cur_list):
            if len(cur_list) == k:
                if c_sum == n:
                    ret.append(cur_list.copy())
                return
            
            if c_sum > n:
                return
            
            for i in range(start_num, 10):
                cur_list.append(i)
                backtracking(i+1, c_sum+i, cur_list)
                cur_list.pop()
        
        backtracking(1, 0, [])
        return ret