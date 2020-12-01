class Solution:
    def shortestPalindrome(self, s: str) -> str:
        p = s + '#' + s[::-1]
        # KMP
        f = [0] * len(p)
        for i in range(1, len(p)):
            t = f[i-1]
            while t > 0 and p[i] != p[t]:
                t = f[t-1]
            if p[i] == p[t]:
                t += 1
            f[i] = t
        # form result
        pre_len = f[-1]
        return s[:pre_len-1:-1]+s


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)