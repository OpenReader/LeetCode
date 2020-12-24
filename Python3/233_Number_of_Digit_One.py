class Solution:
    def countDigitOne(self, n: int) -> int:
        
        def getRest(r, base):
            if r // base > 1:
                return base
            elif r // base == 0:
                return 0
            return r - base
            
        ret = 0
        d = n = n + 1
        base = 1
        while d > 0:
            base *= 10
            r = n % base
            d = (n - r) // 10
            ret += (d + getRest(r ,base//10))
        
        return ret