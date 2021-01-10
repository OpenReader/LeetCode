class Solution:
    # runtime better than 2 hash tables solution
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        return len(s) == len(pattern) and len(set(s)) == len(set(pattern)) and len(set(s)) == len(set(zip(s, pattern)))
    
    # # two hash tables
    # def wordPattern(self, pattern: str, s: str) -> bool:
    #     s2p, p2s = {}, {}
    #     s = s.split(' ')

    #     if len(s) != len(pattern):
    #         return False

    #     for word, c in zip(s, pattern):
    #         if word in s2p:
    #             if s2p[word] != c:
    #                 return False
    #         else:
    #             s2p[word] = c
    #         if c in p2s:
    #             if p2s[c] != word:
    #                 return False
    #         else:
    #             p2s[c] = word
    #     return True