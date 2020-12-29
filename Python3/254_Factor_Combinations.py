class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ret = []
        
        def backtracking(trace, n, start):
            # if n == 1:
            #     if len(trace) > 1:
            #         ret.append(trace.copy())
            #     return
            if trace:
                factors = trace + [n]
                ret.append(factors)
            i = start
            while i * i <= n:
                if n % i == 0:
                    trace.append(i)
                    backtracking(trace, n // i, i)
                    trace.pop()
                i += 1
        
        backtracking([], n, 2)
        return ret