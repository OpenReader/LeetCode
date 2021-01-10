class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        num_cnt = defaultdict(int)
        for a, b in zip(secret, guess):
            if a == b:
                bull += 1
            else:
                num_cnt[a] += 1
        
        for a, b in zip(secret, guess):
            if a != b and b in num_cnt:
                num_cnt[b] -= 1
                cow += 1
                if num_cnt[b] == 0:
                    num_cnt.pop(b)
        
        return str(bull)+'A'+str(cow)+'B'