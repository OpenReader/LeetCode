class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_mis = right_mis = 0
        for c in s:
            if c == '(':
                left_mis += 1
            elif c == ')':
                if left_mis > 0:
                    left_mis -= 1
                elif left_mis == 0:
                    right_mis += 1
                    
        self.ret = set()
        self.s = s
        self.L = len(s)
                    
        def backtrack(index, left_mis, right_mis, left_cnt, right_cnt, expr):
            if left_mis < 0 or right_mis < 0:
                return
            
            if index == self.L:
                if left_mis == 0 and right_mis == 0:
                    self.ret.add(''.join(expr))
                return
            
            if self.s[index] == '(':
                # delete
                backtrack(index+1, left_mis-1, right_mis, left_cnt, right_cnt, expr)
                # keep
                expr.append('(')
                backtrack(index+1, left_mis, right_mis, left_cnt+1, right_cnt, expr)
                expr.pop()
            elif self.s[index] == ')':
                # delete
                backtrack(index+1, left_mis, right_mis-1, left_cnt, right_cnt, expr)
                # keep
                if left_cnt > right_cnt:
                    expr.append(')')
                    backtrack(index+1, left_mis, right_mis, left_cnt, right_cnt+1, expr)
                    expr.pop()
            else:
                # keep
                expr.append(self.s[index])
                backtrack(index+1, left_mis, right_mis, left_cnt, right_cnt, expr)
                expr.pop()
            
            return
        
        backtrack(0, left_mis, right_mis, 0, 0, [])
        
        return list(self.ret)