class Solution:
    # one pass
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        ret = L = len(words)
        
        for i in range(L):
            if words[i] == word1:
                i1 = i
                if i2 >= 0:
                    ret = min(ret, i1 - i2)
            elif words[i] == word2:
                i2 = i
                if i1 >= 0:
                    ret = min(ret, i2 - i1)
        
        return ret
    
#     # two pass
#     def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
#         L = len(words)
        
#         def shortestAfter(w1, w2):
#             ret = L
#             start = -1
#             for i in range(L):
#                 if words[i] == w1:
#                     start = i
#                 if words[i] == w2 and start >= 0:
#                     ret = min(ret, i - start)
#             return ret
        
#         return min(shortestAfter(word1, word2), shortestAfter(word2, word1))