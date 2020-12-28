class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        memo = {}
        operator = {'+': lambda a, b: a+b,
                   '-': lambda a, b: a-b,
                   '*': lambda a, b: a*b}
        
        def combine(l1: List[int], l2: List[int], o: str) -> List[int]:
            f = operator[o]
            ret = []

            for a in l1:
                for b in l2:
                    ret.append(f(a, b))
            return ret
        
        def recursive(s: str) -> List[int]:
            if s in memo:
                return memo[s]
            if s.isdigit():
                memo[s] = [int(s)]
                return memo[s]
            
            L = len(s)
            ret = []
            for i in range(L):
                if s[i] in operator:
                    ret += combine(recursive(s[:i]), recursive(s[i+1:]), s[i])
            
            memo[s] = ret
            return memo[s]
        
        return recursive(input)