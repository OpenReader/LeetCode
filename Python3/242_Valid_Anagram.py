class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_cnt = defaultdict(int)
        for c in s:
            char_cnt[c] += 1
        
        for c in t:
            if c not in char_cnt:
                return False
            char_cnt[c] -= 1
            if char_cnt[c] == 0:
                char_cnt.pop(c)
        
        print(char_cnt)
        return False if char_cnt else True