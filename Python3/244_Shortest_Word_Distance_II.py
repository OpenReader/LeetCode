class WordDistance:

    def __init__(self, words: List[str]):
        self.w_i = {}
        self.L = len(words)
        for i in range(self.L):
            if words[i] not in self.w_i:
                self.w_i[words[i]] = []
            self.w_i[words[i]].append(i)
                

    def shortest(self, word1: str, word2: str) -> int:
        i, j = 0, 0
        l1, l2 = self.w_i[word1], self.w_i[word2]
        m, n = len(l1), len(l2)
        ret = self.L
        while i < m and j < n:
            ret = min(ret, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return ret
                

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)