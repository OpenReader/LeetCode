class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ['0', '1', '8']
        if n == 2:
            return ['11', '88', '69', '96']
        
        pre2 = ['0', '1', '8']
        pre1 = ['00', '11', '88', '69', '96']
        adds = [('1', '1'), ('8', '8'), ('6', '9'), ('9', '6'), ('0', '0')]
        
        for i in range(n-3):
            cur = []
            for s in pre2:
                for a in adds:
                    cur.append(a[0]+s+a[1])
            pre2 = pre1
            pre1 = cur
        
        # last turn:
        cur = []
        adds.pop() # remove (0, 0)
        for s in pre2:
            for a in adds:
                cur.append(a[0]+s+a[1])
        
        return cur