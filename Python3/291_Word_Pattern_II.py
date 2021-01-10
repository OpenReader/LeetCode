class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.p2s, self.seen_s = {}, set()
        self.n, self.m = len(pattern), len(s)
        
        def backtrack(pat_i, s_start, pat, s):
            if pat_i == self.n:
                if s_start == self.m:
                    return True
                return False
            
            if pat[pat_i] in self.p2s:
                exp_s = self.p2s[pat[pat_i]]
                if exp_s == s[s_start: s_start + len(exp_s)] and backtrack(pat_i + 1, s_start + len(exp_s), pat, s):
                    return True
                return False
                
            for i in range(s_start + 1, self.m + 1):
                if s[s_start: i] in self.seen_s:
                    continue
                self.p2s[pat[pat_i]] = s[s_start: i]
                self.seen_s.add(s[s_start: i])
                if backtrack(pat_i + 1, i, pat, s):
                    return True
                self.p2s.pop(pat[pat_i])
                self.seen_s.remove(s[s_start: i])
            
            return False
                
        
        return backtrack(0, 0, pattern, s)