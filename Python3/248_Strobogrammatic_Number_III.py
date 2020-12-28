class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        
        def addRet(nums, length):
            if length < m:
                return 0
            if length == m or length == n:
                acc = 0
                for s in nums:
                    if int(s) >= lo and int(s) <= hi:
                        acc += 1
                return acc
            # m < length < n
            return len(nums)
            
        m, n = len(low), len(high)
        lo, hi = int(low), int(high)
        
        ret = addRet(['0', '1', '8'], 1)
        ret += addRet(['11', '88', '69', '96'], 2) if n >= 2 else 0

        pre2 = ['0', '1', '8']
        pre1 = ['00', '11', '88', '69', '96']
        adds = [('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]

        for i in range(n-2):
            cur = []
            for s in pre2:
                for a in adds:
                    cur.append(a[0]+s+a[1])
            ret += addRet(cur, i + 3)
            # add ('0', '0') for next turn
            for s in pre2:
                cur.append('0'+s+'0')
            pre2 = pre1
            pre1 = cur

        return ret