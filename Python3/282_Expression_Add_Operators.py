class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        self.target = target
        self.L = len(num)
        self.num = num
        self.ret = []
        
        def calculate(track):
            # print(track)
            sk = []
            for c in reversed(track):
                if c == '+' or c == '-' or c == '*':
                    sk.append(c)
                else:
                    if sk and sk[-1] == '*':
                        sk.pop()
                        a = int(sk.pop())
                        sk.append(str(a * int(c)))
                    else:
                        sk.append(c)
            
            ret = int(sk.pop())
            while sk:
                o = sk.pop()
                a = int(sk.pop())
                if o == '+':
                    ret += a
                else:
                    ret -= a
            
            return ret        
        
        def backtracking(track, i):
            if len(track[-1]) > 1 and track[-1][0] == '0':
                return
            if i == self.L:
                if calculate(track) == self.target:
                    self.ret.append(''.join(track))
                return
            
            backtracking(track + ['+', self.num[i]], i+1)
            backtracking(track + ['-', self.num[i]], i+1)
            backtracking(track + ['*', self.num[i]], i+1)
            
            last_num = track[-1]
            last_num_ex = last_num + self.num[i]
            track[-1] = last_num_ex
            backtracking(track, i+1)
            track[-1] = last_num
            
            return
        
        if self.L == 0:
            return self.ret
        
        backtracking([self.num[0],], 1)
        
        return self.ret