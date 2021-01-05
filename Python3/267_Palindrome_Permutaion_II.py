class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # char-count map
        cnt = {}
        odd_s = set()
        for c in s:
            cnt[c] = cnt.setdefault(c, 0) + 1
            if c in odd_s:
                odd_s.remove(c)
            else:
                odd_s.add(c)

        cur_s = ''
        if len(odd_s) > 1:
            return []
        elif len(odd_s) == 1:
            cur_s = odd_s.pop()
            cnt[cur_s] -= 1
            if cnt[cur_s] == 0:
                cnt.pop(cur_s)
        
        ret = []
        def backtracking(cur_s: str, remain_num: int):
            if remain_num == 0:
                ret.append(cur_s)
                return
            
            for c in cnt:
                if cnt[c] != 0:
                    cnt[c] -= 2
                    if cnt[c] == 0:
                        remain_num -= 1
                    backtracking(c+cur_s+c, remain_num)
                    if cnt[c] == 0:
                        remain_num += 1
                    cnt[c] += 2
        
        backtracking(cur_s, len(cnt))
        return ret