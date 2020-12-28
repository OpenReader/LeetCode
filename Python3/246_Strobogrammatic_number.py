class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        L = len(num)
        mid = L // 2
        stronum = {'1', '8', '0'}
        for i in range(mid):
            if num[i] != num[L-i-1]:
                if num[i] == '6' and num[L-i-1] == '9' or num[i] == '9' and num[L-i-1] == '6':
                    continue
                return False
            elif num[i] not in stronum:
                return False
        
        return True if L % 2 == 0 else num[mid] in stronum