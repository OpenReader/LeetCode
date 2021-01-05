class Solution:
    
    # recursive solution
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        if num <= 0:
            return False
        factors = [2, 3, 5]
        
        def dfs(num):
            if num in factors:
                return True
        
            for f in factors:
                if num % f == 0 and dfs(num//f):
                    return True
            
            return False
        
        return dfs(num)

        # # iteration solution (not perform better)
        # def isUgly(self, num: int) -> bool:
        #     if num <= 0:
        #         return False
            
        #     while num % 2 == 0:
        #         num //= 2
        #     while num % 3 == 0:
        #         num //= 3
        #     while num % 5 == 0:
        #         num //= 5
            
        #     return num == 1