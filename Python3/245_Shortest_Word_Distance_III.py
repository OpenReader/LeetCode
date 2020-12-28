class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        L = len(words)
        i1, i2 = -1, -1
        ret = L
        for i in range(L):
            if words[i] == word1:
                i1 = i
                if i2 != -1:
                    ret = min(ret, i1-i2)
            if words[i] == word2:
                i2 = i
                if i1 != -1 and i1 != i2:
                    ret = min(ret, i-i1)
        
        return ret