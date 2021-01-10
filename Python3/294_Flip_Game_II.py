class Solution:
        
    def canWin(self, s: str) -> bool:
        memo= {}
        def dfs(s):
            if s in memo:
                return memo[s]
            
            for i in range(1, len(s)):
                if s[i-1] == '+' and s[i] == '+':
                    if not self.canWin(s[:i-1]+'-'+s[i+1:]):
                        memo[s] = True
                        return True
            
            memo[s] = False
            return False

        return dfs(s)