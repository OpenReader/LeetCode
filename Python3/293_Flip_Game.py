class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ret  = []
        L = len(s)
        for i in range(1, L):
            if s[i-1] == '+' and s[i] == '+':
                flip_s = list(s)
                flip_s[i-1] = flip_s[i] = '-'
                ret.append(''.join(flip_s))
        return ret